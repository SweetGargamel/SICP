test = {
  'name': 'Question 3: Trees',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> t = Tree(1, Tree(2))
          f41e02308aca9727300aa755c805de15
          # locked
          >>> t = Tree(1, [Tree(2)])
          >>> t.label
          da81f4f42959407c9278f93fd99650cc
          # locked
          >>> t.branches[0]
          7624f47c9caae17d34ebfe710b9ecd90
          # locked
          >>> t.branches[0].label
          95a89c1fab7d23c3f4b45a0e6bcbc6df
          # locked
          >>> t.label = t.branches[0].label
          >>> t
          c5a38801a4c87eeed680e5409bc046dc
          # locked
          >>> t.branches.append(Tree(4, [Tree(8)]))
          >>> len(t.branches)
          95a89c1fab7d23c3f4b45a0e6bcbc6df
          # locked
          >>> t.branches[0]
          7624f47c9caae17d34ebfe710b9ecd90
          # locked
          >>> t.branches[1]
          fc7f047df0784e9002c2aac6abd15ab1
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
