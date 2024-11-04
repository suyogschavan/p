pragma solidity >= 0.5.0 < 0.9.0; 
contract Loops 
{ 
uint [3] public arr; uint public count; 
function Whileloop() public 
{ 
while(count < arr.length) 
{ 
arr[count] = count; count++; 
} 
} 
function Forloop() public { 
    for(uint i=count; i<arr.length; i++) 
    { 
    arr[count] = count; 
    count++; 
    } 
}}