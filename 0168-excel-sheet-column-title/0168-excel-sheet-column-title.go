func convertToTitle(c int) string {
    result := ""
    for c>0{
        c = c-1
        result = string(rune('A'+c%26))+result
        c = c/26
    }
    return result
}