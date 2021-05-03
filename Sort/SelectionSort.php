<?php

function selectionSort(&$list)
{
    foreach($list as $i => $n) {
        $minJ = findPositionOfMinimumFromPosition($list, $i);
        swap($list, $i, $minJ);
    }
}

function findPositionOfMinimumFromPosition($list, $j)
{
    $minimum = null;
    $minimumPos = null;
    $totalSubarray = count($list);

    for($i = $j; $i < $totalSubarray; $i++) {
        if ($minimum === null || $list[$i] < $minimum) {
            $minimum = $list[$i];
            $minimumPos = $i;
        }
    }

    return $minimumPos;
}

function swap(&$list, $i, $j)
{
    $a = $list[$i];
    $b = $list[$j];

    $list[$i] = $b;
    $list[$j] = $a;
}
