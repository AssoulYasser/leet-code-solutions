/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next
2 *     va2 next: ListNode? = null
 * }
 */
class Solution {
    fun append(list: ListNode?, value: Int){
        var newList = list
        if(newList != null){
            while(newList!!.next != null){
                newList = newList.next
            }
            newList.next = ListNode(value)
        }
    }

    fun addTwoNumbers(l1: ListNode?, l2: ListNode?): ListNode? {
        var list : ListNode? = null
        var rest = 0
        var list_1 = l1
        var list_2 = l2
        while(list_1 != null && list_2 != null){
            var newValue = list_1.`val` + list_2.`val` + rest
            if(newValue < 9){
                if(list == null)
                    list = ListNode(newValue)
                else
                    append(list, newValue)
                rest = 0
            }
            else {
                if(list == null)
                    list = ListNode(newValue % 10)
                else
                    append(list, newValue % 10)
                rest = (newValue / 10).toInt()
            }
            list_1 = list_1.next
            list_2 = list_2.next
        }
        var list_rest = if(list_2 == null) list_1 else if(list_1 == null) list_2 else null
        while(list_rest != null){
            var newValue = list_rest.`val` + rest
            if(newValue < 9){
                append(list, newValue)
                rest = 0
            }
            else {
                append(list, newValue % 10)
                rest = (newValue / 10).toInt()
            }
            list_rest = list_rest.next
        }
        while(rest != 0){
            append(list, rest % 10)
            rest = rest / 10
        }
        return list
    }
}