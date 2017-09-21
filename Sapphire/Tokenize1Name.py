#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Tokenize1Name')
def gem():
    show = 0


    def tokenize_name__X__newline(m):
        j = qj()
        s = qs()

        name_end = m.end('name')

        r = conjure_identifier(s[j : name_end])

        if qd() is not 0:
            suffix = conjure_whitespace_line(s[name_end : ])

            if qi() == qj():
                r = evoke_identifier_whitespace(r, suffix)
            else:
                prefix = s[qi() : qj()]

                r = BookcaseIdentifier(
                        (conjure_whitespace_line   if '\n' in prefix else   conjure_whitespace)(prefix),
                        r,
                        suffix,
                    )

            skip_tokenize_prefix()

            return r

        wn(conjure_token_newline(s[name_end : ]))

        if qi() == j:
            return r

        prefix = s[qi() : j]

        return evoke_whitespace_identifier(
                   (conjure_whitespace_line   if '\n' in prefix else   conjure_whitespace)(prefix),
                   r,
               )


    @share
    def tokenize_name():
        assert qk() is none
        assert qn() is none

        j = qj()
        s = qs()

        m = name_ow_match(s, j)

        if m is none:
            raise_unknown_line()

        if m.start('comment_newline') is not -1:
            return tokenize_name__X__newline(m)

        name_end = m.end('name')

        r = conjure_identifier(s[j : name_end])

        if qi() != j:
            r = evoke_whitespace_identifier(conjure_whitespace(s[qi() : j]), r)

        wi(name_end)
        wj(m.end())

        return r
