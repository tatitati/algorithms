<?php

$data = [9, 500, 2, 30, 1, 80, 123];


function splitLeftAndRight($list)
{
    $midX = floor(count($list)/2);

    return [
        array_slice($list, 0, $midX),
        array_slice($list, $midX),
    ];
}

function merge($left, $right)
{
    $mergedList = [];

    while(count($left) + count($right) > 0) {
        if (count($left) == 0) {
            $mergedList[] = $right[0];
            array_shift($right);
            continue;
        }

        if (count($right) == 0) {
            $mergedList[] = $left[0];
            array_shift($left);
            continue;
        }

        if ($left[0] < $right[0]) {
            $mergedList[] = $left[0];
            array_shift($left);
            continue;
        }

        $mergedList[] = $right[0];
        array_shift($right);
    }

    return $mergedList;
}

function mergeSort($list)
{
    if (count($list) < 2) {
        return $list;
    }

    list($left, $right) = splitLeftAndRight($list);
    return merge(mergeSort($left), mergeSort($right));
}

/**
 * @test split
 */
$listA = [9, 500, 2, 30, 1];
list($left, $right) = splitLeftAndRight($listA);
assert($left === [9, 500]);
assert($right === [2, 30, 1]);



$listA = [9, 500, 2, 30];
list($left, $right) = splitLeftAndRight($listA);
assert($left === [9, 500]);
assert($right === [2, 30]);

/**
 * @test merge
 */
$listA = [9];
$listB = [];
assert(merge($listA, $listB) == [9]);



$listA = [100];
$listB = [8];
assert(merge($listA, $listB) == [8, 100]);



$listA = [3, 100];
$listB = [8];
assert(merge($listA, $listB) == [3, 8, 100]);

/**
 * @test mergeSort
 */
$listA = [3, 100, 8];
assert(mergeSort($listA) == [3, 8, 100]);



$listA = [3, 100, 8, 15, 500];
assert(mergeSort($listA) == [3, 8, 15, 100, 500]);