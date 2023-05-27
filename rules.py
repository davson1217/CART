# Note that these rules are for the transcription of Yoruba letters to Lithuanian

letter_a_context_rules = [
    {
        # [A] succeeded by [N] triggers a nasal sound. e.g., IK[AN]
        # Note that this rule may fail to produce a wrong transcription if preceded by a vowel letter
        'is_vowel': 'Yes',
        'letter': 'A',
        'preceded_by_N': 'Yes',
        'succeeded_by_N': 'No',
        'transcription': 'O',
    },
    {
        # [A] will always be pronounced /O/ if preceded by [N]. e.g., IYAN[A]
        'is_vowel': 'Yes',
        'letter': 'A',
        'preceded_by_N': 'No',
        'succeeded_by_N': 'Yes',
        'transcription': 'O',
    },
    {
        # Free-context letter [A]
        'is_vowel': 'Yes',
        'letter': 'A',
        'preceded_by_N': 'No',
        'succeeded_by_N': 'No',
        'transcription': 'A',
    },
    {
        # detects long sound e.g F[A]AGUN
        'is_vowel': 'Yes',
        'letter': 'A',
        'preceded_by_N': 'No',
        'succeeded_by_N': 'No',
        'succeeded_by_same_letter': 'Yes',
        'transcription': 'Ą',
    },
    {
        # removes second character of a long letter e.g., BA[A]YANNI
        'is_vowel': 'Yes',
        'letter': 'A',
        'preceded_by_N': 'No',
        'succeeded_by_N': 'No',
        'preceded_by_same_letter': 'Yes',
        'transcription': '',
    }
]
letter_e_context_rules = [
    {
        # [E] is context-free
        'is_vowel': 'Yes',
        'letter': 'E',
        'preceded_by_N': 'Yes',
        'succeeded_by_N': 'No',
        'transcription': 'E',
    },
    {
        'is_vowel': 'Yes',
        'letter': 'E',
        'preceded_by_N': 'No',
        'succeeded_by_N': 'Yes',
        'transcription': 'E',
    },
    {
        'is_vowel': 'Yes',
        'letter': 'E',
        'preceded_by_N': 'No',
        'succeeded_by_N': 'No',
        'transcription': 'E',
    },
    {
        'is_vowel': 'Yes',
        'letter': 'E',
        'preceded_by_N': 'No',
        'succeeded_by_N': 'No',
        'succeeded_by_same_letter': 'Yes',
        'transcription': 'EE',
    },
    {
        'is_vowel': 'Yes',
        'letter': 'E',
        'preceded_by_N': 'No',
        'succeeded_by_N': 'No',
        'preceded_by_same_letter': 'Yes',
        'transcription': '',
    }
]
letter_e__context_rules = [
    {
        # [E] is context-free
        'is_vowel': 'Yes',
        'letter': 'Ẹ',
        'preceded_by_N': 'Yes',
        'succeeded_by_N': 'No',
        'transcription': 'Ẹ',
    },
    {
        'is_vowel': 'Yes',
        'letter': 'Ẹ',
        'preceded_by_N': 'No',
        'succeeded_by_N': 'Yes',
        'transcription': 'Ẹ',
    },
    {
        'is_vowel': 'Yes',
        'letter': 'Ẹ',
        'preceded_by_N': 'No',
        'succeeded_by_N': 'No',
        'transcription': 'Ẹ',
    },
    {
        'is_vowel': 'Yes',
        'letter': 'Ẹ',
        'preceded_by_N': 'No',
        'succeeded_by_N': 'No',
        'succeeded_by_same_letter': 'Yes',
        'transcription': 'ẸẸ',
    },
    {
        'is_vowel': 'Yes',
        'letter': 'Ẹ',
        'preceded_by_N': 'No',
        'succeeded_by_N': 'No',
        'preceded_by_same_letter': 'Yes',
        'transcription': '',
    }
]
letter_i_context_rules = [
    {
        # [E] is context-free
        'is_vowel': 'Yes',
        'letter': 'I',
        'preceded_by_N': 'Yes',
        'succeeded_by_N': 'No',
        'transcription': 'I',
    },
    {
        'is_vowel': 'Yes',
        'letter': 'I',
        'preceded_by_N': 'No',
        'succeeded_by_N': 'Yes',
        'transcription': 'I',
    },
    {
        'is_vowel': 'Yes',
        'letter': 'I',
        'preceded_by_N': 'No',
        'succeeded_by_N': 'No',
        'transcription': 'I',
    },
    {
        'is_vowel': 'Yes',
        'letter': 'I',
        'preceded_by_N': 'No',
        'succeeded_by_N': 'No',
        'succeeded_by_same_letter': 'Yes',
        'transcription': 'II',
    },
    {
        'is_vowel': 'Yes',
        'letter': 'I',
        'preceded_by_N': 'No',
        'succeeded_by_N': 'No',
        'preceded_by_same_letter': 'Yes',
        'transcription': '',
    }
]
letter_o_context_rules = [
    {
        # [E] is context-free
        'is_vowel': 'Yes',
        'letter': 'O',
        'preceded_by_N': 'Yes',
        'succeeded_by_N': 'No',
        'transcription': 'O',
    },
    {
        'is_vowel': 'Yes',
        'letter': 'O',
        'preceded_by_N': 'No',
        'succeeded_by_N': 'Yes',
        'transcription': 'O',
    },
    {
        'is_vowel': 'Yes',
        'letter': 'O',
        'preceded_by_N': 'No',
        'succeeded_by_N': 'No',
        'transcription': 'O',
    },
    {
        'is_vowel': 'Yes',
        'letter': 'O',
        'preceded_by_N': 'No',
        'succeeded_by_N': 'No',
        'succeeded_by_same_letter': 'Yes',
        'transcription': 'OO',
    },
    {
        'is_vowel': 'Yes',
        'letter': 'O',
        'preceded_by_N': 'No',
        'succeeded_by_N': 'No',
        'preceded_by_same_letter': 'Yes',
        'transcription': '',
    }
]
letter_o__context_rules = [
    {
        'is_vowel': 'Yes',
        'letter': 'Ọ',
        'preceded_by_N': 'Yes',
        'succeeded_by_N': 'No',
        'transcription': 'O',
    },
    {
        'is_vowel': 'Yes',
        'letter': 'Ọ',
        'preceded_by_N': 'No',
        'succeeded_by_N': 'Yes',
        'transcription': 'O',
    },
    {
        'is_vowel': 'Yes',
        'letter': 'Ọ',
        'preceded_by_N': 'No',
        'succeeded_by_N': 'No',
        'transcription': 'O',
    },
    {
        'is_vowel': 'Yes',
        'letter': 'Ọ',
        'preceded_by_N': 'No',
        'succeeded_by_N': 'No',
        'succeeded_by_same_letter': 'Yes',
        'transcription': 'O',
    },
    {
        'is_vowel': 'Yes',
        'letter': 'Ọ',
        'preceded_by_N': 'No',
        'succeeded_by_N': 'No',
        'preceded_by_same_letter': 'Yes',
        'transcription': '',
    },
]

letter_u_context_rules = [
    {
        # [E] is context-free
        'is_vowel': 'Yes',
        'letter': 'U',
        'preceded_by_N': 'Yes',
        'succeeded_by_N': 'No',
        'transcription': 'U',
    },
    {
        'is_vowel': 'Yes',
        'letter': 'U',
        'preceded_by_N': 'No',
        'succeeded_by_N': 'Yes',
        'transcription': 'U',
    },
    {
        'is_vowel': 'Yes',
        'letter': 'U',
        'preceded_by_N': 'No',
        'succeeded_by_N': 'No',
        'transcription': 'U',
    },
    {
        'is_vowel': 'Yes',
        'letter': 'U',
        'preceded_by_N': 'No',
        'succeeded_by_N': 'No',
        'succeeded_by_same_letter': 'Yes',
        'transcription': 'UU',
    },
    {
        'is_vowel': 'Yes',
        'letter': 'U',
        'preceded_by_N': 'No',
        'succeeded_by_N': 'No',
        'preceded_by_same_letter': 'Yes',
        'transcription': '',
    },
]
vowel_glide_rules = [
    {
        'letter': 'A',
        'is_vowel': 'Yes',
        'preceded_by_I': 'Yes',
        'transcription': 'JA',
    },
    {
        'letter': 'E',
        'is_vowel': 'Yes',
        'preceded_by_I': 'Yes',
        'transcription': 'JE',
    },
    {
        'letter': 'Ẹ',
        'is_vowel': 'Yes',
        'preceded_by_I': 'Yes',
        'transcription': 'JẸ',
    },
    {
        'letter': 'O',
        'is_vowel': 'Yes',
        'preceded_by_I': 'Yes',
        'transcription': 'JO',
    },
    {
        'letter': 'Ọ',
        'is_vowel': 'Yes',
        'preceded_by_I': 'Yes',
        'transcription': 'JỌ',
    },
    {
        'letter': 'U',
        'is_vowel': 'Yes',
        'preceded_by_I': 'Yes',
        'transcription': 'JU',
    },
]
context_free_rules = [
    {
        'letter': 'B',
        'transcription': 'B'
    },
    {
        'letter': 'D',
        'transcription': 'D'
    },
    {
        'letter': 'F',
        'transcription': 'F'
    },
    {
        'letter': 'G',
        'transcription': 'G'
    },
    {
        'letter': 'GB',
        'transcription': 'GB'
    },
    {
        'letter': 'H',
        'transcription': 'H'
    },
    {
        'letter': 'J',
        'transcription': 'DŽ'
    },
    {
        'letter': 'K',
        'transcription': 'K'
    },
    {
        'letter': 'L',
        'transcription': 'L'
    },
    {
        'letter': 'M',
        'transcription': 'M'
    },
    {
        'letter': 'N',
        'transcription': 'N'
    },
    {
        'letter': 'P',
        'transcription': 'P'
    },
    {
        'letter': 'R',
        'transcription': 'R'
    },
    {
        'letter': 'S',
        'transcription': 'S'
    },
    {
        'letter': 'Ṣ',
        'transcription': 'Š'
    },
    {
        'letter': 'T',
        'transcription': 'T'
    },
    {
        'letter': 'W',
        'transcription': 'V'
    },
    {
        'letter': 'Y',
        'transcription': 'J'
    },
]

all_rules = letter_e__context_rules + letter_o__context_rules + letter_i_context_rules + letter_o_context_rules \
            + letter_e_context_rules + letter_u_context_rules + letter_a_context_rules + context_free_rules \
            + vowel_glide_rules

yoruba_vowels = ["A", "E", "Ẹ", "I", "O", "Ọ", "U"]
yoruba_letters = ["A", "B", "D", "E", "Ẹ", "F",  "G", "GB",  "H", "I",  "J",  "K",  "L",  "M",  "N", "O", "Ọ", "P",
                  "R",  "S",  "Ṣ", "T", "U", "W",  "Y"]
encodings = [0, 1, 2, 3, 23, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 24, 15, 16, 17, 22, 18, 19, 20, 21]
