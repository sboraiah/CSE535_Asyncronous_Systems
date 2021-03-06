# -*- generated by 1.0.12 -*-
import da
PatternExpr_199 = da.pat.TuplePattern([da.pat.ConstantPattern('request'), da.pat.FreePattern('c2'), da.pat.FreePattern('p')])
PatternExpr_224 = da.pat.TuplePattern([da.pat.ConstantPattern('release'), da.pat.BoundPattern('_BoundPattern227_'), da.pat.BoundPattern('_BoundPattern228_')])
PatternExpr_257 = da.pat.TuplePattern([da.pat.ConstantPattern('ack'), da.pat.BoundPattern('_BoundPattern260_'), da.pat.BoundPattern('_BoundPattern261_')])
PatternExpr_305 = da.pat.TuplePattern([da.pat.ConstantPattern('request'), da.pat.FreePattern('c'), da.pat.FreePattern('p')])
PatternExpr_392 = da.pat.TuplePattern([da.pat.ConstantPattern('done'), da.pat.BoundPattern('_BoundPattern395_')])
PatternExpr_419 = da.pat.TuplePattern([da.pat.ConstantPattern('done')])
PatternExpr_424 = da.pat.BoundPattern('_BoundPattern426_')
PatternExpr_398 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)]), da.pat.TuplePattern([da.pat.ConstantPattern('done'), da.pat.BoundPattern('_BoundPattern408_')])])
PatternExpr_427 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.BoundPattern('_BoundPattern433_')]), da.pat.TuplePattern([da.pat.ConstantPattern('done')])])
PatternExpr_231 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)]), da.pat.TuplePattern([da.pat.ConstantPattern('release'), da.pat.BoundPattern('_BoundPattern241_'), da.pat.BoundPattern('_BoundPattern242_')])])
PatternExpr_264 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)]), da.pat.TuplePattern([da.pat.ConstantPattern('ack'), da.pat.BoundPattern('_BoundPattern274_'), da.pat.BoundPattern('_BoundPattern275_')])])
PatternExpr_509 = da.pat.TuplePattern([da.pat.ConstantPattern('done'), da.pat.BoundPattern('_BoundPattern512_')])
PatternExpr_515 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)]), da.pat.TuplePattern([da.pat.ConstantPattern('done'), da.pat.BoundPattern('_BoundPattern525_')])])
_config_object = {'channel': 'fifo', 'clock': 'Lamport'}
import sys
import time
import timeit

class P(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._PReceivedEvent_0 = []
        self._PReceivedEvent_1 = []
        self._PReceivedEvent_2 = []
        self._PReceivedEvent_4 = []
        self._PReceivedEvent_5 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_0', PatternExpr_199, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_1', PatternExpr_224, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_2', PatternExpr_257, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_3', PatternExpr_305, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_304]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_4', PatternExpr_392, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_5', PatternExpr_419, sources=[PatternExpr_424], destinations=None, timestamps=None, record_history=True, handlers=[])])

    def setup(self, ts2, s, nrequests, **rest_531):
        super().setup(ts2=ts2, s=s, nrequests=nrequests, **rest_531)
        self._state.ts2 = ts2
        self._state.s = s
        self._state.nrequests = nrequests
        pass

    def run(self):

        def task():
            self.output('in cs')
            self.output('releasing cs')
        t1 = time.process_time()
        t11 = timeit.default_timer()
        for i in range(self._state.nrequests):
            self.mutex(task)
        t2 = time.process_time()
        t22 = timeit.default_timer()
        self.send(('performance', (t2 - t1), (t22 - t11), self._id), to=self._state.ts2)
        self.send(('done', self._id), to=self._state.s)
        super()._label('_st_label_383', block=False)
        p = None

        def UniversalOpExpr_384():
            nonlocal p
            for p in self._state.s:
                if (not PatternExpr_398.match_iter(self._PReceivedEvent_4, _BoundPattern408_=p, SELF_ID=self._id)):
                    return False
            return True
        _st_label_383 = 0
        while (_st_label_383 == 0):
            _st_label_383 += 1
            if UniversalOpExpr_384():
                _st_label_383 += 1
            else:
                super()._label('_st_label_383', block=True)
                _st_label_383 -= 1
        self.send(('done', self._id), to=self.parent())
        super()._label('_st_label_416', block=False)
        _st_label_416 = 0
        while (_st_label_416 == 0):
            _st_label_416 += 1
            if PatternExpr_427.match_iter(self._PReceivedEvent_5, _BoundPattern433_=self.parent(), SELF_ID=self._id):
                _st_label_416 += 1
            else:
                super()._label('_st_label_416', block=True)
                _st_label_416 -= 1
        self.output('terminating')

    def mutex(self, task):
        super()._label('request', block=False)
        c = self.logical_clock()
        self.send(('request', c, self._id), to=self._state.s)
        super()._label('_st_label_195', block=False)
        p = c2 = None

        def UniversalOpExpr_197():
            nonlocal p, c2
            for (_, _, (_ConstantPattern216_, c2, p)) in self._PReceivedEvent_0:
                if (_ConstantPattern216_ == 'request'):
                    if (not (PatternExpr_231.match_iter(self._PReceivedEvent_1, _BoundPattern241_=c2, _BoundPattern242_=p, SELF_ID=self._id) or ((c, self._id) < (c2, p)))):
                        return False
            return True
        p = None

        def UniversalOpExpr_250():
            nonlocal p
            for p in self._state.s:
                if (not PatternExpr_264.match_iter(self._PReceivedEvent_2, _BoundPattern274_=c, _BoundPattern275_=p, SELF_ID=self._id)):
                    return False
            return True
        _st_label_195 = 0
        while (_st_label_195 == 0):
            _st_label_195 += 1
            if (UniversalOpExpr_197() and UniversalOpExpr_250()):
                _st_label_195 += 1
            else:
                super()._label('_st_label_195', block=True)
                _st_label_195 -= 1
        super()._label('critical_section', block=False)
        self.send(('cs', 'in', c, self._id), to=self._state.ts2)
        task()
        self.send(('cs', 'out', c, self._id), to=self._state.ts2)
        super()._label('release', block=False)
        self.send(('release', c, self._id), to=self._state.s)

    def _P_handler_304(self, c, p):
        self.send(('ack', c, self._id), to=p)
    _P_handler_304._labels = None
    _P_handler_304._notlabels = None

class Node_(da.NodeProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._Node_ReceivedEvent_0 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_Node_ReceivedEvent_0', PatternExpr_509, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[])])

    def run(self):
        nprocs = (int(sys.argv[1]) if (len(sys.argv) > 1) else 10)
        nrequests = (int(sys.argv[2]) if (len(sys.argv) > 2) else 1)
        ps = self.new(P, num=nprocs)
        for p in ps:
            self._setup(p, ((ps - {p}), nrequests))
        self._start(ps)
        super()._label('_st_label_501', block=False)
        p = None

        def UniversalOpExpr_502():
            nonlocal p
            for p in ps:
                if (not PatternExpr_515.match_iter(self._Node_ReceivedEvent_0, _BoundPattern525_=p)):
                    return False
            return True
        _st_label_501 = 0
        while (_st_label_501 == 0):
            _st_label_501 += 1
            if UniversalOpExpr_502():
                _st_label_501 += 1
            else:
                super()._label('_st_label_501', block=True)
                _st_label_501 -= 1
        self.send(('done',), to=ps)
