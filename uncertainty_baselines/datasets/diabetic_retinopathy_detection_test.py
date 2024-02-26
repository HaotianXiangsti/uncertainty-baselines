# coding=utf-8
# Copyright 2024 The Uncertainty Baselines Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for Kaggle diabetic retinopathy detection."""

import tensorflow as tf
import uncertainty_baselines as ub


class DiabeticRetinopathyDetectionDatasetTest(ub.datasets.DatasetTest):

  def testDatasetSize(self):
    super()._testDatasetSize(
        ub.datasets.UBDiabeticRetinopathyDetectionDataset,
        image_size=(512, 512, 3))


if __name__ == "__main__":
  tf.test.main()
