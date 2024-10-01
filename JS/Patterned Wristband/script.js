function checkVertical(arr) {
    inner_len = arr[0].length
    for (i = 0; i < inner_len; i++) {
        temp_char = ''
        temp_sum = 0
        for (j = 0; j < arr.length; j++) {
            temp_char = arr[j][i]
            temp_sum += temp_char.charCodeAt()
        }
        if (temp_sum != arr.length * temp_char.charCodeAt()) {
            return false
        }
    }
    return true
}

function checkHorizontal(arr) {
    inner_len = arr[0].length
    for (i = 0; i < arr.length; i++) {
        temp_char = ''
        temp_sum = 0
        for (j = 0; j < inner_len; j++) {
            temp_char = arr[i][j]
            temp_sum += temp_char.charCodeAt()
        }
        if (temp_sum != inner_len * temp_char.charCodeAt()) {
            return false
        }
    }
    return true
}

function checkLeftDiagonal(arr) {
    inner_len = arr[0].length
    for (j = 1; j < arr.length; j++) {
        for (i = 1; i < inner_len; i++) {
            if (arr[j - 1][i - 1] != arr[j][i]) {
                return false
            }
        }
    }
    return true
}

function checkRightDiagonal(arr) {
    inner_len = arr[0].length
    for (j = 1; j < arr.length; j++) {
        for (i = 1; i < inner_len; i++) {
            if (arr[j - 1][i] != arr[j][i - 1]) {
                return false
            }
        }
    }
    return true
}

//test area
document.getElementById('msg').innerHTML = (function () {
    if (
        checkLeftDiagonal([
            ['A', 'B', 'C'],
            ['C', 'A', 'B'],
            ['B', 'C', 'A'],
            ['A', 'B', 'C'],
        ])
    ) {
        return 'Good job!'
    }
    return 'Ah shit!'
})()