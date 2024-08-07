class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'

        num_to_str = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety'
        }

        answer = []
        digit_names = [
            'Billion',
            'Million',
            'Thousand',
            ''
        ]

        for i in range(len(digit_names)):
            power = (10**((3 * (len(digit_names) - 1)) - 3*i))
            cur_digit = num // power
            num %= power

            if cur_digit > 0:
                if cur_digit >= 100:
                    answer.append(num_to_str[cur_digit // 100])
                    answer.append('Hundred')
                    cur_digit %= 100
                if cur_digit >= 20:
                    answer.append(num_to_str[cur_digit // 10 * 10])
                    cur_digit %= 10
                if cur_digit > 0:
                    answer.append(num_to_str[cur_digit])
                if i < len(digit_names) - 1:
                    answer.append(digit_names[i])

        return ' '.join(answer)




