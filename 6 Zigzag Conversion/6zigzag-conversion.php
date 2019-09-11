class Solution {

    /**
     * @param String $s
     * @param Integer $numRows
     * @return String
     */
    function convert($s, $numRows) {
        if ($numRows == 1) {
            return $s;
        }
        
        $count = strlen($s);
        $level = 0;
        $direction = 1;
        $stack = [];
    
        for ($i = 0; $i < $count; $i++) {
            $stack[$level] = ($stack[$level] ?? '') . $s[$i];
            
            $level += $direction;
            
            if ($level >= $numRows) {
                $level = $numRows - 2;
                $direction = -1;
                continue;
            }
            
            if ($level < 0) {
                $level = $numRows == 1 ? 0 : 1;
                $direction = 1;
                continue;
            }
        }
        
        $result = '';
        foreach ($stack as $line) {
            $result .= $line;
        }
        
        return $result;
    }
}