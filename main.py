import random

file = open('dictionary.txt', 'a', encoding="utf-8")

characters = [
    '﷽', '񴀒', 'n', '淼', '򝸣', '䜑', '繓', '딟', 'y', '慑', '', 'Ҽ', '񖧸', '䨿', '姕', 'i'
    'Ǣ', '󆂼', '򛾝', 'Ж', 'ҋ', '𤞞', '#', '@', '𪞺', 'ӳ',  '썐', '𥖁', '灱', '픿', '䧁', '嫰',
    'X', '򈖓', 'ԗ', '܋衣', '癐', '摃', '􅑲', '杗', '�', 'q', '点', '慟', '卥', '遲', '%', '坳',
    '֠0', '蹬', 'ܷ茶', 'Σ', 'ʞ', '󱪻', 'Ũ', '㏯', '𙨡', 'Ͼ', 'h', '΍', '񼱅', '㹈', '򑃒', '؀', '􂱎',
    '݅䂱', 't', 'ॶ', 'v', '𧌑', '󚡂', '񂍰', 'Ѓ', '󙝂', '𗧔', '@', 'Į', 'g', 'q', '_', 'ૺ', '򀟒', '焾',
    '񩦱', 'o', 'ᆒ', '<', '񑎾', '񈘵', 'ʤ', 'ʑ', '腞', '􈵻', '慴', '񦑙', '9', 'o', 'ա', 'Q', 'j', 'ʠ'
]

print('Generating dictionary...')

for i in range(50000):
    name = ""
    for var in range(150):
        name += characters[random.randint(0, len(characters) - 1)]
    file.write(name)

file.close()
print('Dictionary generated successfully')
