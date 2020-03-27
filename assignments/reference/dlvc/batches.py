
from .dataset import Dataset
from .ops import Op

import typing

class Batch:
    '''
    A (mini)batch generated by the batch generator.
    '''

    def __init__(self):
        '''
        Ctor.
        '''

        self.data = None
        self.label = None
        self.idx = None

class BatchGenerator:
    '''
    Batch generator.
    Returned batches have the following properties:
      data: numpy array holding batch data of shape (s, SHAPE_OF_DATASET_SAMPLES).
      label: numpy array holding batch labels of shape (s, SHAPE_OF_DATASET_LABELS).
      idx: numpy array with shape (s,) encoding the indices of each sample in the original dataset.
    '''

    def __init__(self, dataset: Dataset, num: int, shuffle: bool, op: Op=None):
        '''
        Ctor.
        Dataset is the dataset to iterate over.
        num is the number of samples per batch. the number in the last batch might be smaller than that.
        shuffle controls whether the sample order should be preserved or not.
        op is an operation to apply to input samples.
        Raises TypeError on invalid argument types.
        Raises ValueError on invalid argument values, such as if num is > len(dataset).
        '''

        # TODO implement

        pass

    def __len__(self) -> int:
        '''
        Returns the number of batches generated per iteration.
        '''

        # TODO implement

        pass

    def __iter__(self) -> typing.Iterable[Batch]:
        '''
        Iterate over the wrapped dataset, returning the data as batches.
        '''

        # TODO implement
        # The "yield" keyword makes this easier

        pass
