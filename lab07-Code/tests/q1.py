test = {
  'name': 'Question 1: Repr-esentation',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> class A:
          ...     def __init__(self, x):
          ...         self.x = x
          ...     def __repr__(self):
          ...         return self.x
          ...     def __str__(self):
          ...         return self.x * 2
          >>> class B:
          ...     def __init__(self):
          ...         print('boo!')
          ...         self.a = []
          ...     def add_a(self, a):
          ...         self.a.append(a)
          ...     def __repr__(self):
          ...         print(len(self.a))
          ...         ret = ''
          ...         for a in self.a:
          ...              ret += str(a)
          ...         return ret
          >>> A('one')
          da54f7462380e1e9436f2c15b6d039f4
          # locked
          >>> print(A('one'))
          479b536aeac29eec7e2fa71e1971b128
          # locked
          >>> repr(A('two'))
          9f5916884cadc291915b64cbb024af24
          # locked
          >>> b = B()
          6c4b215a1976c229cc7c03e0be27941e
          # locked
          >>> b.add_a(A('a'))
          >>> b.add_a(A('b'))
          >>> b
          95a89c1fab7d23c3f4b45a0e6bcbc6df
          0021c69e12d053c2001d26a445f32992
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
