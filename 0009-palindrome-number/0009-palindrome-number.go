import (
    "fmt"
    
)
func isPalindrome(x int) bool {
    left := 0
    hi := strconv.Itoa(x)
    fmt.Println(hi)
    right := len(hi)-1
    for left<right{
        if hi[left] != hi[right]{
            return false
        }
        left+=1
        right-=1
    }
    return true
}