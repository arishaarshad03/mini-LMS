class Range:
    def __init__ (self, start, stop = None, step=1):

        if isinstance (start, Range):
            self._start = start._start
            self._stop = start._stop
            self._step = start._step
            self._length = start._length

        else:
        # validates the step
            self._step = self._validate_step(step)
            self._start, self._stop = self._init_bounds(start,stop)
            self._length = self._calc_length()
        
    # ----------HELPER METHODS----------
    def _validate_step(self, step):
        # ensures that step is not zero
        if step == 0:
            raise ValueError("step cannot be 0")
        return step
    
    def _init_bounds(self, start, stop):
        # is only 1 arg is provided
        if stop is None:
            stop = start
            start = 0
        return start, stop
    
    def _calc_length(self):
        # calculates the number of elements and handles both positive and negative steps
        if self._step > 0:
            return max(0, (self._stop - self._start + self._step -1)// self._step)
        else:
            return max(0, (self._stop - self._start + self._step + 1)// self._step)
        
    # ----------SPECIAL METHODS----------
    def __len__(self):
        # number of elements in range
        return self._length
    
    def __getitem__(self,k):
        # returns the element at index k (supports neg indexes too)
        if k < 0:
            k = k + self._length
        if not 0 <= k < self._length:
            raise IndexError("index out of range")

        return self._start + k * self._step

    def __iter__(self):
        index = 0
        while index < len(self):
            yield self[index]
            index += 1

    def __str__(self):
        result = []
        i = 0
        while i < len(self):
            result.append(self[i])
            i += 1
        return str(result)
