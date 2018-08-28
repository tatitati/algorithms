<?php

function displayLab($lab)
{
    foreach($lab as $i=>$columns) {
        echo "\n";
        foreach($columns as $j => $value) {
            echo " $value ";
        }
        echo "\n";
    }
}

function isWall($lab, $i, $j) {
    if (!isset($lab[$i]) || !isset($lab[$i][$j])) {
        return true;
    }

    return $lab[$i][$j] === 0;
}

function isExit($lab, $i, $j) {
    return $lab[$i][$j] === 'EXIT';
}

function isVisited($lab, $i, $j) {
    return $lab[$i][$j] === 'X';
}

function isInvalidMovement($from, $to)
{
    // invalid if is moving in diagonal
    if ($from['x'] !== $to[0] && $from['y'] !== $to[1]) {
        return true;
    }

    // invalid if is moving more than one step;
    if (abs($from['x'] - $to[0]) > 1 || abs($from['y'] - $to[1]) > 1) {
        return true;
    }

    return false;
}



function solveLaberinth($lab, &$solution, $start)
{
    $currentX= $start['x'];
    $currentY= $start['y'];

    for ($r=$currentX-1; $r<= $currentX+1; $r++) {
        for ($c=$currentY-1; $c<= $currentY+1; $c++) {
            if (isWall($lab, $r, $c) || isVisited($solution, $r, $c) || isInvalidMovement($start, [$r, $c])) {
                continue;
            }

            if (isExit($lab, $r, $c)) {
                $solution[$r][$c] = 'X';
                return true;
            }

            $solution[$r][$c] = 'X';
            if (solveLaberinth($lab, $solution, ['x' => $r, 'y' => $c])) {
                return true;
            }

            // backgracking here (undo)
            $solution[$r][$c] = 0;
        }
    }

    return false;
}


/**
 * @test valid movements
 */
$labA = [
    [0,   0,   0],
    [0, 'A', 'C'],
    [0,   0,   0]
];
assert(false == isWall($labA, 1, 1));
assert(true == isWall($labA, 0, 0));



$labA = [
    [0,   0,   0],
    [0, 'X', 'X'],
    [0,   0,   0]
];
assert(true == isVisited($labA, 1, 1));
assert(false == isVisited($labA, 0, 0));



// cannot move more than one step
assert(true == isInvalidMovement(['x' => 1, 'y' => 1], [1, 3]));
// cannot move in diagonal
assert(true == isInvalidMovement(['x' => 1, 'y' => 1], [0, 2]));
// can move in x,y axis one step
assert(false == isInvalidMovement(['x' => 1, 'y' => 1], [1, 2]));


/**
 * @test solution
 */

 $lab = [
    [0, 'A',   0, 'R',   0,  0,    0],
    [0, 'B', 'C', 'D', 'E', 'F',   0],
    [0,   0,   0,   0,   0, 'H',   0],
    [0,   0, 'N', 'M', 'L', 'I',   0],
    [0,   0, 'Q',   0,   0, 'J', 'EXIT'],
    [0,   0,   0,   0,   0,  0,    0],
];

$solution = [
    [0, 'X',   0,   0,   0,  0,    0],
    [0,   0,   0,   0,   0,  0,    0],
    [0,   0,   0,   0,   0,  0,    0],
    [0,   0,   0,   0,   0,  0,    0],
    [0,   0,   0,   0,   0,  0,    0],
    [0,   0,   0,   0,   0,  0,    0],
];

solveLaberinth($lab, $solution, ['x' => 0, 'y' => 1]);
assert([
    [0, 'X',   0,   0,   0,   0,   0],
    [0, 'X', 'X', 'X', 'X', 'X',   0],
    [0,   0,   0,   0,   0, 'X',   0],
    [0,   0,   0,   0,   0, 'X',   0],
    [0,   0,   0,   0,   0, 'X', 'X'],
    [0,   0,   0,   0,   0,  0,    0],
] == $solution);