#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Copyright (c) Merchise Autrement [~º/~] and Contributors
# All rights reserved.
#
# This is free software; you can do what the LICENCE file allows you to.
#
import doctest
from dataclasses import dataclass
from typing import Any, Generic, Sequence, TypeVar

import pytest
from hypothesis import given
from hypothesis import strategies as s
from hypothesis.strategies import SearchStrategy

import xotless.immutables
from xotless.immutables import ImmutableWrapper

from .support import captured_stderr, captured_stdout


def test_doctests():
    with captured_stdout() as stdout, captured_stderr() as stderr:
        failure_count, test_count = doctest.testmod(
            xotless.immutables,
            verbose=True,
            optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS,
            raise_on_error=False,
        )
    if test_count and failure_count:  # pragma: no cover
        print(stdout.getvalue())
        print(stderr.getvalue())
        raise AssertionError("ImmutableWrapper doctest failed")


def test_wrap_callable():
    class Bar:
        def return_self(self):
            return self

    class Foo(Bar):
        pass

    obj = Foo()
    wrapper = ImmutableWrapper(obj)
    assert wrapper.return_self() is obj

    wrapper2 = ImmutableWrapper(obj, wrap_callables=True)
    assert wrapper2.return_self() is wrapper2


def test_wrap_properties():
    from dataclasses import dataclass
    from datetime import datetime, timedelta

    @dataclass(frozen=True)
    class Commodity:
        start_date: datetime
        duration: timedelta

        @property
        def end_date(self):
            return self.start_date + self.duration

    now = datetime.utcnow()
    day = timedelta(1)
    item = ImmutableWrapper(Commodity(None, None), wrap_descriptors=True).replace(
        start_date=now, duration=day
    )
    assert item.end_date == now + day

    commodity = Commodity(datetime.utcnow(), timedelta(1))
    assert hash(commodity) == hash(ImmutableWrapper(commodity))


def test_wrap_descriptors():
    class Descriptor:
        def __get__(self, instance, owner):
            if instance is None:
                return self
            return id(instance)

    class Item:
        identity = Descriptor()

    item = ImmutableWrapper(Item(), wrap_descriptors=True)
    assert item.identity == id(item)


anything: SearchStrategy[Any] = s.integers() | s.floats() | s.text()
anything = anything | s.dictionaries(s.text(), anything) | s.tuples(anything) | s.lists(anything)

sequences = s.lists(anything) | s.tuples(anything)


@dataclass
class Obj:
    truth: bool
    calls: int = 0

    def __bool__(self):
        self.calls += 1
        return self.truth


@given(anything)
def test_boolean_values_basic(val):
    assert bool(ImmutableWrapper(val)) == bool(val)


@given(s.from_type(Obj))
def test_boolean_values_custom_method(val: Obj):
    val.calls = 0
    assert bool(ImmutableWrapper(val)) == bool(val)
    assert val.calls == 2


T = TypeVar("T")


@dataclass
class Container(Generic[T]):
    seq: Sequence[T]
    calls: int = 0

    def __len__(self):
        self.calls += 1
        return len(self.seq)

    def __iter__(self):
        self.calls += 1
        return iter(self.seq)


@given(s.builds(Container, seq=sequences, calls=s.just(0)))
def test_len_custom_method(val: Container):
    assert len(ImmutableWrapper(val)) == len(val) == len(val.seq)
    assert val.calls == 2


@dataclass
class CustomIterable(Generic[T]):
    seq: Sequence[T]
    calls: int = 0

    def __iter__(self):
        self.calls += 1
        return iter(self.seq)


@given(s.builds(CustomIterable, seq=sequences, calls=s.just(0)))
def test_iter_custom_method(val: CustomIterable):
    assert isinstance(list(ImmutableWrapper(val)), list)
    assert val.calls == 1


@dataclass
class NonContainer:
    id: str


@given(s.from_type(NonContainer))
def test_len_raises_typeerror_for_non_len(val):
    with pytest.raises(TypeError):
        len(val)


@given(s.from_type(NonContainer))
def test_iter_raises_typeerror_for_non_len(val):
    with pytest.raises(TypeError):
        iter(val)
