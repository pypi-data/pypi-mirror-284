# Swahili Tokenization

- I will update the readme.md with more information

## Syllabic Tokenization with Byte Fallback
- Syllabic Tokenization with Byte Fallbacks allows the foreign elements in the text.
- Inspiration through SentencePiece. <sup> Will add citation </sup>
- The resultant vocabulary size is small, approximately 1200.
### Syllabic Tokenization
- Kiswahili is a syllabic language
- Tokenizes a sentence on the 219 Kiswahili syllables
- I hypothesize that it'll allow the model to be syllable-aware.
<small> I will provide more information concerning the syllabic language and references later </small>

### Byte Fallback
- To items that do not appear as a syllable, they fallback to the utf-8 representation of the character
- Allows tokenization of non-swahili elements that appear in the sentence. Simple example an English name such as john ('jo', ?)
- Fallbacks to unknown token when all comes to nothing.

## Example Usage:
I will add some examples