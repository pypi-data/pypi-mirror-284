from __future__ import annotations

from abc import ABCMeta, abstractmethod

from bob.pipelines import Sample


class Database(metaclass=ABCMeta):
    """Base database class for PAD experiments."""

    @abstractmethod
    def fit_samples(self) -> list[Sample]:
        """Returns :any:`bob.pipelines.Sample`'s to train a PAD model.

        Returns
        -------
        samples : list
            List of samples for model training.
        """
        pass

    @abstractmethod
    def predict_samples(self, group: str = "dev") -> list[Sample]:
        """Returns :any:`bob.pipelines.Sample`'s to be scored.

        Parameters
        ----------
        group : :py:class:`str`, optional
            Limits samples to this group

        Returns
        -------
        samples : list
            List of samples to be scored.
        """
        pass

    def all_samples(
        self, groups: str | list[str] | None = None
    ) -> list[Sample]:
        """Returns all the samples of the database in one list.

        Giving ``groups`` will restrict the ``predict_samples`` to those groups.
        """
        samples = self.fit_samples()
        if groups is not None:
            if type(groups) is str:
                groups = [groups]
            for group in groups:
                samples.extend(self.predict_samples(group=group))
        else:
            samples.extend(self.predict_samples(group=group))
        return samples
