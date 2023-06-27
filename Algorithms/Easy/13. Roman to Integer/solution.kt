class Solution {
    
    fun isRoman(s:String):Boolean{

        for(i in s) {

            if (i != 'I' && i != 'V' && i != 'X' && i != 'L' && i != 'C' && i != 'D' && i != 'M') {
                return false
            }
        }
        return true
    }

    fun toInt(c:Char) : Int{
        when(c){
            'I' -> return 1
            'V' -> return 5
            'X' -> return 10
            'L' -> return 50
            'C' -> return 100
            'D' -> return 500
            'M' -> return 1000
            else -> return 0
        }
    }

    fun romanToInt(s: String): Int {
        
        var result = 0
        var i = 0
        while(i < s.length-1){
            if(toInt(s[i]) >= toInt(s[i+1])){
                result += toInt(s[i])
                i += 1
            }
            else{
                val inter = toInt( s[i+1] )- toInt( s[i])
                result += inter
                i += 2
            }
        }

        if(i < s.length)
            result += toInt(s[i])

        return result
    }
}