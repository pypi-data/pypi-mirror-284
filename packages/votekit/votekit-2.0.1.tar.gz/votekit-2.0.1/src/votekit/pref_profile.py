from __future__ import annotations
import csv
from fractions import Fraction
import pandas as pd
from pydantic import BaseModel, validator
from typing import Optional
import numpy as np
from .ballot import Ballot


class PreferenceProfile(BaseModel):
    """
    PreferenceProfile class, contains ballots and candidates for a given election.

    Args:
        ballots (list[Ballot]): List of ``Ballot`` objects.
        candidates (list, optional): List of candidate strings. Defaults to None.


    Attributes:
        ballots (list[Ballot]): List of ``Ballot`` objects.
        candidates (list, optional): List of candidate strings.
        df (pandas.DataFrame): pandas ``DataFrame`` used to store ballots.
    """

    ballots: list[Ballot] = []
    candidates: Optional[list] = None
    df: pd.DataFrame = pd.DataFrame()

    @validator("candidates", allow_reuse=True)
    def cands_must_be_unique(cls, candidates: list) -> list:
        if not len(set(candidates)) == len(candidates):
            raise ValueError("All candidates must be unique")
        return candidates

    def get_ballots(self) -> list[Ballot]:
        """
        Returns:
            list: List of ``Ballot`` objects.
        """
        return self.ballots[:]

    def get_candidates(self, received_votes: Optional[bool] = True) -> list:
        """
        Args:
            received_votes (bool, optional): If True, only return candidates that received votes.
                Defaults to True.
        Returns:
            list: List of candidates.
        """

        if received_votes or not self.candidates:
            unique_cands: set = set()
            for ballot in self.ballots:
                unique_cands.update(*ballot.ranking)

            return list(unique_cands)
        else:
            return self.candidates

    # can also cache
    def num_ballots(self) -> Fraction:
        """
        Counts number of ballots based on assigned weight.

        Returns:
            Fracton: Number of ballots cast.
        """
        num_ballots = Fraction(0)
        for ballot in self.ballots:
            num_ballots += ballot.weight

        return num_ballots

    def to_dict(self, standardize: bool = False) -> dict:
        """
        Converts profile to dictionary with keys = rankings and
        values = corresponding total weights.

        Args:
            standardize (bool, optional): If True, divides the weight of each ballot by the total
                weight. Defaults to False.

        Returns:
            dict: A dictionary with ranking (keys) and corresponding total weights (values).
        """
        num_ballots = self.num_ballots()
        di: dict = {}
        for ballot in self.ballots:
            rank_tuple = tuple(next(iter(item)) for item in ballot.ranking)
            if standardize:
                weight = ballot.weight / num_ballots
            else:
                weight = ballot.weight
            if rank_tuple not in di.keys():
                di[rank_tuple] = weight
            else:
                di[rank_tuple] += weight
        return di

    class Config:
        arbitrary_types_allowed = True

    def to_csv(self, fpath: str):
        """
        Saves PreferenceProfile to CSV.

        Args:
            fpath (str): Path to the saved csv.
        """
        with open(fpath, "w", newline="") as csvfile:
            fieldnames = ["weight", "ranking"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for ballot in self.ballots:
                writer.writerow({"weight": ballot.weight, "ranking": ballot.ranking})

    def _create_df(self) -> pd.DataFrame:
        """
        Creates pandas DataFrame for display and building plots.

        Returns:
            pandas.DataFrame: Data frame of ballots with weight and percent columns.
        """
        weights = []
        ballots = []
        for ballot in self.ballots:
            part = []
            for ranking in ballot.ranking:
                if len(ranking) == 1:
                    part.append(list(ranking)[0])

                else:
                    part.append(f"{ranking} (Tie)")

            ballots.append(tuple(part))
            weights.append(ballot.weight)

        df = pd.DataFrame({"Ballots": ballots, "Weight": weights})

        try:
            df["Percent"] = df["Weight"] / df["Weight"].sum()
        except ZeroDivisionError:
            df["Percent"] = np.nan

        # fill nans with zero for edge cases
        df["Percent"] = df["Percent"].fillna(0.0)

        def format_as_percent(frac):
            return f"{float(frac):.2%}"

        df["Percent"] = df["Percent"].apply(format_as_percent)
        return df.reset_index(drop=True)

    def head(
        self,
        n: int,
        sort_by_weight: Optional[bool] = True,
        percents: Optional[bool] = False,
        totals: Optional[bool] = False,
    ) -> pd.DataFrame:
        """
        Displays top-n ballots in profile.

        Args:
            n (int): Number of ballots to view.
            sort_by_weight (bool, optional): If True, rank ballot from most to least votes.
                Defaults to True.
            percents (bool, optional): If True, show voter share for a given ballot.
                Defaults to False.
            totals (bool, optional): If True, show total values for Percent and Weight.
                Defaults to False.

        Returns:
            pd.DataFrame: A dataframe with top-n ballots.
        """
        if self.df.empty:
            self.df = self._create_df()

        if sort_by_weight:
            df = (
                self.df.sort_values(by="Weight", ascending=False)
                .head(n)
                .reset_index(drop=True)
            )
        else:
            df = self.df.head(n).reset_index(drop=True)

        if totals:
            df = self._sum_row(df)

        if not percents:
            return df.drop(columns="Percent")

        return df

    def tail(
        self,
        n: int,
        sort_by_weight: Optional[bool] = True,
        percents: Optional[bool] = False,
        totals: Optional[bool] = False,
    ) -> pd.DataFrame:
        """
        Displays bottom-n ballots in profile.

        Args:
            n (int): Number of ballots to view.
            sort_by_weight (bool, optional): If True, rank ballot from least to most votes.
                Defaults to True.
            percents (bool, optional): If True, show voter share for a given ballot.
                Defaults to False.
            totals (bool, optional): If True, show total values for Percent and Weight.
                Defaults to False.

        Returns:
            A data frame with bottom-n ballots.
        """

        if self.df.empty:
            self.df = self._create_df()

        if sort_by_weight:
            df = self.df.sort_values(by="Weight", ascending=True)
            df["New Index"] = [x for x in range(len(self.df) - 1, -1, -1)]
            df = df.set_index("New Index").head(n)
            df.index.name = None

        else:
            df = self.df.iloc[::-1].head(n)

        if totals:
            df = self._sum_row(df)

        if not percents:
            return df.drop(columns="Percent")

        return df

    def __str__(self) -> str:
        # Displays top 15 cast ballots or entire profile

        if self.df.empty:
            self.df = self._create_df()

        if len(self.df) < 15:
            return self.head(n=len(self.df), sort_by_weight=True).to_string(
                index=False, justify="justify"
            )

        print(
            f"PreferenceProfile too long, only showing 15 out of {len(self.df) } rows."
        )
        return self.head(n=15, sort_by_weight=True).to_string(
            index=False, justify="justify"
        )

    # set repr to print outputs
    __repr__ = __str__

    def condense_ballots(self) -> PreferenceProfile:
        """
        Groups ballots by rankings and updates weights.

        Returns:
            PreferenceProfile: A PreferenceProfile object with condensed ballot list.
        """
        ranking_to_index: dict = {}
        weight_accumulator = {}

        for ballot in self.ballots:
            if ballot.ranking not in ranking_to_index:
                ranking_to_index[ballot.ranking] = len(ranking_to_index)
                weight_accumulator[ballot.ranking] = Fraction(0)

            weight_accumulator[ballot.ranking] += ballot.weight

        new_ballot_list = [
            Ballot(ranking=tuple(map(frozenset, ranking)), weight=weight)
            for ranking, weight in weight_accumulator.items()
        ]

        condensed_profile = PreferenceProfile(ballots=new_ballot_list)
        return condensed_profile

    def __eq__(self, other):
        if not isinstance(other, PreferenceProfile):
            return False
        pp_1 = self.condense_ballots()
        pp_2 = other.condense_ballots()
        for b in pp_1.ballots:
            if b not in pp_2.ballots:
                return False
        for b in pp_2.ballots:
            if b not in pp_1.ballots:
                return False
        return True

    def _sum_row(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Computes sum total for weight and percent column
        """

        def format_as_float(percent_str):
            return float(percent_str.split("%")[0])

        sum_row = {
            "Ballot": "",
            "Weight": f'{df["Weight"].sum()} out of {self.num_ballots()}',
            "Percent": f'{df["Percent"].apply(format_as_float).sum():.2f} out of 100%',
        }

        df.loc["Totals"] = sum_row  # type: ignore

        return df.fillna("")

    def __add__(self, other):
        """
        Add two PreferenceProfiles by combining their ballot lists.
        """
        if isinstance(other, PreferenceProfile):
            ballots = self.ballots + other.ballots
            pp = PreferenceProfile(ballots=ballots)
            pp.condense_ballots()
            return pp
        else:
            raise TypeError(
                "Unsupported operand type. Must be an instance of PreferenceProfile."
            )
