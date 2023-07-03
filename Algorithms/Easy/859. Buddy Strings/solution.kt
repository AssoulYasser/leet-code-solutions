class Solution {

    fun has_same_length(s: String, goal:String): Boolean{
        return s.length == goal.length
    }

    fun are_equal(s: String, goal:String): Boolean{
        return s == goal
    }

    fun has_same_char_in_diff_index(s: String): Boolean{
        var index = 0
        val len = s.length
        for(char in s){
            val new_index = index + 1
            if(s.indexOf(char, startIndex=new_index) != -1)
                return true

            index += 1
        }
        
        return false
    }

    fun switch_characters(str: String, index1: Int, index2: Int): String {
        val charArray = str.toCharArray()
        val temp = charArray[index1]
        charArray[index1] = charArray[index2]
        charArray[index2] = temp
        return String(charArray)
    }

    fun get_indices(str: String, str2: String, char: Char, startIndex: Int): List<Int> {
    val indices = mutableListOf<Int>()
    var index = str.indexOf(char, startIndex)
    
    while (index != -1) {
        if(str[index] != str2[index])
            indices.add(index)
        index = str.indexOf(char, index + 1)
    }
    
    return indices
}


    fun buddyStrings(s: String, goal: String): Boolean {
        if(!has_same_length(s, goal))
            return false

        if(are_equal(s, goal))
            return has_same_char_in_diff_index(s)
        
        var s_index = 0
        for(s_char in s){
            val goal_indeces = get_indices(goal, s, s_char, s_index)
            for(index in goal_indeces)
                if(switch_characters(s, s_index, index) == goal)
                    return true
            s_index += 1
        }

        return false

    }
}