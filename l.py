class Op:
    V = 'V'
    A = 'A'
    S = 'S'

class Lambda:
    def __init__(self, left, op, right):
        self._L = left
        self._Op = op
        self._R = right
    @property
    def Op(self):
        return self._Op
    @property
    def L(self):
        return self._L
    @property
    def R(self):
        return self._R
    def __str__(self):
        if self._Op == Op.V:
            return self._R
        if self._Op == Op.A:
            return '(L' + str(self.L) + '.' + (str(self.R)) + ')'
        return "(" + str(self.L) + ')(' + str(self.R) + ")"

V = Lambda('', Op.V, 'x')
print(V)
lx = Lambda('x', Op.A, V)
print(lx)
a = Lambda(V, Op.S, V)
print(a)
H = Lambda(V, Op.A, a)
print(H)
Y = Lambda(H, Op.S, H)
print(Y)
