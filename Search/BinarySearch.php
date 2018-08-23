<?php
function binarySearch($list, $target)
{
    $lowIdx = 0;
    $highIdx = count($list)-1;

    while ($lowIdx <= $highIdx) {
        $midIdx = floor(($lowIdx + $highIdx)/2);
        if ($target > $list[$midIdx]) {
            $lowIdx = $midIdx + 1;
            continue;
        }

        if ($target < $list[$midIdx]) {
            $highIdx = $midIdx-1;
            continue;
        }

        return $midIdx;
    }

    return -1;
}

/**
 * @test
 */
$list = [];
assert(binarySearch($list, 6) == -1);

$list = [6];
assert(binarySearch($list, 6) == 0);

$list = [6 ,8];
assert(binarySearch($list, 8) == 1);

$list = [6, 8, 23, 30, 34, 45, 60, 110];
assert(binarySearch($list, 34) == 4);

$list = [6, 8, 34];
assert(binarySearch($list, 999) == -1);