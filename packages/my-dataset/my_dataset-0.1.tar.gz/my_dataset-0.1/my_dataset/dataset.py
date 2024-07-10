import tensorflow as tf
import numpy as np
import os

def load_image_dataset_from_directory(directory_path, img_height, img_width, batch_size):
    dataset = tf.keras.preprocessing.image_dataset_from_directory(
        directory_path,
        image_size=(img_height, img_width),
        batch_size=batch_size
    )
    return dataset

def dataset_to_numpy(dataset):
    images = []
    labels = []
    for image_batch, label_batch in dataset:
        images.append(image_batch.numpy())
        labels.append(label_batch.numpy())
    images = np.concatenate(images)
    labels = np.concatenate(labels)
    return images, labels

def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))

def _int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))

def serialize_example(image, label):
    feature = {
        'image': _bytes_feature(tf.io.encode_jpeg(image).numpy()),
        'label': _int64_feature(label),
    }
    example_proto = tf.train.Example(features=tf.train.Features(feature=feature))
    return example_proto.SerializeToString()

def write_tfrecord(images, labels, filename):
    with tf.io.TFRecordWriter(filename) as writer:
        for image, label in zip(images, labels):
            tf_example = serialize_example(image, label)
            writer.write(tf_example)

def load_tfrecord_dataset(file_pattern, batch_size):
    def parse_tfrecord_fn(example):
        feature_description = {
            'image': tf.io.FixedLenFeature([], tf.string),
            'label': tf.io.FixedLenFeature([], tf.int64),
        }
        example = tf.io.parse_single_example(example, feature_description)
        image = tf.io.decode_jpeg(example['image'], channels=1)
        label = example['label']
        return image, label

    files = tf.data.Dataset.list_files(file_pattern)
    dataset = files.interleave(tf.data.TFRecordDataset, cycle_length=4)
    dataset = dataset.map(parse_tfrecord_fn, num_parallel_calls=tf.data.experimental.AUTOTUNE)
    dataset = dataset.batch(batch_size)
    dataset = dataset.prefetch(buffer_size=tf.data.experimental.AUTOTUNE)
    return dataset
