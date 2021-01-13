class Sort {

    bubbleSort (arr) {
        for (let i = 0; i < arr.length; i++) {
            for (let j = i+1; j < arr.length; j++) {
                if (arr[i] > arr[j]) {
                    let temp = arr[j];
                    arr[j] = arr[i];
                    arr[i] = temp;
                }
            }
        }
        return arr;
    }

    selectionSort (arr) {
        for (let i = 0; i < arr.length; i++) {
            let smallest_ind = i;
            for (let j = i; j < arr.length; j++) {
                if (arr[j] < arr[smallest_ind])
                    smallest_ind = j;
            }
            let temp = arr[smallest_ind];
            arr[smallest_ind] = arr[i];
            arr[i] = temp;
        }
        return arr;
    }

    insertionSort (arr) {
        for (let i = 1; i < arr.length; i++) {
            // scenario 1: if current number is larger than left
            // leave it at this place
            if (arr[i] > arr[i-1]) continue;
            // scenario 2: if current number is smaller than the left
            // take out this number
            const item = arr.splice(i, 1)[0];
            // find the index to insert this item
            for (let j = 0; j < i; j++) {
                if (arr[j] > item) {
                    // put it to the indexing placing
                    arr.splice(j, 0, item);
                    break;
                }
            }
        }
        return arr;
    }

    mergeSort (arr) {
        // define function merge that returns a merge step of left and right
        const merge = (left, right) => {
            const result = [];
            let leftIndex = 0;
            let rightIndex = 0;
            // compare through each item in left and right
            while (leftIndex < left.length && rightIndex < right.length) {
                if (left[leftIndex] < right[rightIndex]) {
                    result.push(left[leftIndex]);
                    leftIndex++;
                } else {
                    result.push(right[rightIndex]);
                    rightIndex++;
                }
            }
            // concat the remaining items to the result array (one of left or right now is empty)
            // and return this result
            return result.concat(left.slice(leftIndex)).concat(right.slice(rightIndex));
        }
        // base case if the subarray length 1
        if (arr.length === 1) {
            return arr;
        }
        // split array into right and left
        const half_length = Math.ceil(arr.length / 2);
        const left = arr.slice(0, half_length);
        const right = arr.slice(half_length);
        // resursion step
        return merge(this.mergeSort(left), this.mergeSort(right));
    }

    quickSort (arr, left, right) {
        // Inputs: array to besorted, pointers of left and right
        if (left < right) {
            const divider = partition(arr, left, right);

            this.quickSort(arr, left, divider-1);
            this.quickSort(arr, divider+1, right);
        }
        
        return arr;

        /* This function takes last element as pivot,
           places the pivot element at its correct position in sorted array, 
           and places all smaller (smaller than pivot) to left of pivot 
           and all greater elements to right of pivot */
        function partition (array, low, high) {
            let pivot = high;      // picked the last item as pivot
            let divider = low;       // use the first as the initial index of divider
            // iterate through left to the right of array
            for (let i = low; i < high-1; i++) {
                if (array[i] < arr[pivot]) {
                    // swap divider and current items
                    swap(array, divider, i);
                    // move the divider to the next item
                    // increment divider means create a space for the pivot to stay
                    divider++;
                }
            }
            // after come through all items from left to right-1
            // we can put the rightest pivot to the next place of divider
            swap(array, divider, pivot);
            
            return divider;

            function swap(array_swap, first, second) {
                const temp = array_swap[first];
                array_swap[first] = array_swap[second];
                array_swap[second] = temp;
            }
        }
    }

};

const numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];

const mySort = new Sort();
//const result = mySort.mergeSort(numbers);
const result = mySort.quickSort(numbers, 0, numbers.length -1);
console.log(result);