class Solution {

    /**
     * @param Integer $num
     * @return String
     */
    function intToRoman($num) {
        $result = '';

        if ($num < 0 || $num > 3999) {
            return $result;
        }

        $table = [
            'M' => 1000,
            'CM' => 900,
            'D' => 500,
            'CD' => 400,
            'C' => 100,
            'XC' => 90,
            'L' => 50,
            'XL' => 40,
            'X' => 10,
            'IX' => 9,
            'V' => 5,
            'IV' => 4,
            'I' => 1,
        ];

        foreach ($table as $key => $value) {
            while ($num >= $value) {
                $num = $num - $value;
                $result .= $key;
            }
        }

        return $result;
    }
}