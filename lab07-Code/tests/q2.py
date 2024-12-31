test = {
  'name': 'Question 2: Linked Lists',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> link = Link(1000)
          >>> link.first
          7de129e686c7015ae3f783dc90228395
          # locked
          >>> link.rest is Link.empty
          dbd62a2b84fc780e75072f865cd27813
          # locked
          >>> link = Link(1000, 2000)
          f41e02308aca9727300aa755c805de15
          # locked
          >>> link = Link(1000, Link())
          f41e02308aca9727300aa755c805de15
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> link = Link(1, Link(2, Link(3)))
          >>> link.first
          da81f4f42959407c9278f93fd99650cc
          # locked
          >>> link.rest.first
          95a89c1fab7d23c3f4b45a0e6bcbc6df
          # locked
          >>> link.rest.rest.rest is Link.empty
          dbd62a2b84fc780e75072f865cd27813
          # locked
          >>> link.first = 9001
          >>> link.first
          756ef6aa6ac810d083a547d9c2c2ef8a
          # locked
          >>> link.rest = link.rest.rest
          >>> link.rest.first
          26a1d710165f25a963c130fc14aa7596
          # locked
          >>> link = Link(1)
          >>> link.rest = link
          >>> link.rest.rest.rest.rest.first
          da81f4f42959407c9278f93fd99650cc
          # locked
          >>> link = Link(2, Link(3, Link(4)))
          >>> link2 = Link(1, link)
          >>> link2.first
          da81f4f42959407c9278f93fd99650cc
          # locked
          >>> link2.rest.first
          95a89c1fab7d23c3f4b45a0e6bcbc6df
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> link = Link(5, Link(6, Link(7)))
          >>> link
          e604739886395aea0bd1ab8e3a3981b3
          # locked
          >>> print(link)
          598d47bd1b63dc596d17ca1b4a62529e
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
