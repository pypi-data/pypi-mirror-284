#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import json


class Paginator(object):
    def __init__(self, total=0, size=10, current=1, split=10):
        self._current = current
        self._first = 1
        self._last = 1
        self._previous = 1
        self._next = 1
        self._offset = 1
        self._size = size
        self._pages = 1
        self._total = total
        self._split = split
        self._previous_split = 0
        self._next_split = split
        self._currents = []
        self._results = []

    @property
    def current(self):
        if int(self._current) < 1:
            self._current = 1
        if int(self._current) >= int(self.pages):
            self._current = self.pages
        return self._current

    @property
    def first(self):
        self._first = 1
        return self._first

    @property
    def last(self):
        self._last = int(self.pages)
        return self._last

    @property
    def previous(self):
        current = int(self.current)
        previous = current - 1
        if previous < 1:
            previous = 1
        self._previous = previous
        return self._previous

    @property
    def next(self):
        current = int(self.current)
        pages = int(self.pages)
        next = current + 1
        if next > pages:
            next = pages
        self._next = next
        return self._next

    @property
    def offset(self):
        current = int(self.current)
        size = int(self.size)
        offset = (current - 1) * size
        if int(offset) < 0:
            offset = 0
        self._offset = offset
        return self._offset

    @property
    def size(self):
        if int(self._size) <= 0:
            self._size = 10
        return self._size

    @property
    def pages(self):
        pages = 1
        total = int(self.total)
        size = int(self.size)
        if total % size == 0:
            pages = int(total / size)
        else:
            pages = int(total / size) + 1
        if int(pages) < 1:
            pages = 1
        self._pages = pages
        return self._pages

    @property
    def total(self):
        if int(self._total) <= 0:
            self._total = 0
        return self._total

    @property
    def split(self):
        if int(self._split) <= 0:
            self._split = 10
        return self._split

    @property
    def previous_split(self):
        if int(self.current) < int(self.split):
            self._previous_split = 1
        else:
            self._previous_split = int((int(self.current) / int(self.split))) * int(self.split)
        return self._previous_split

    @property
    def next_split(self):
        if int(self.current) < int(self.split):
            self._next_split = int(self.split) + 1
        else:
            self._next_split = int((int(self.current) / int(self.split))) * int(self.split) + int(self.split)
        if int(self._next_split) >= int(self.pages):
            self._next_split = int((int(self.pages) / int(self.split))) * int(self.split)
        return self._next_split

    @property
    def currents(self):
        if int(self.pages) <= int(self.split):
            self._currents = [i + 1 for i in range(int(self.pages))]
        else:
            if int(self.current) < int(self.split):
                self._currents = [i + 1 for i in range(int(self.split))]
            else:
                if int(self.previous_split) == int(self.next_split):
                    self._currents = [i + 1 for i in
                                      range(int(self.previous_split) - int(self.split), int(self.previous_split))]
                else:
                    self._currents = [i + 1 for i in range(self.previous_split, int(self.next_split))]
        return self._currents

    @property
    def results(self):
        return self._results

    @results.setter
    def results(self, value=[]):
        self._results = value

    def to_dict(self):
        return {
            "current": self.current,
            "first": self.first,
            "last": self.last,
            "previous": self.previous,
            "next": self.next,
            "offset": self.offset,
            "size": self.size,
            "pages": self.pages,
            "total": self.total,
            "split": self.split,
            "previous_split": self.previous_split,
            "next_split": self.next_split,
            "currents": self.currents,
            "results": self.results,
        }

    def to_json(self):
        return json.dumps(self.to_dict())
