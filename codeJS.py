



Array.html // 1. Write a JavaScript function to check whether an `input` is an array or not. 
// Test Data :
// console.log(is_array('w3resource'));
// console.log(is_array([1, 2, 4, 0]));
// false
// true


// 2. Write a JavaScript function to clone an array. 
// Test Data :
// console.log(array_Clone([1, 2, 4, 0]));
// console.log(array_Clone([1, 2, [4, 0]]));
// [1, 2, 4, 0]
// [1, 2, [4, 0]]


// 3. Write a JavaScript function to get the first element of an array. Passing a parameter 'n' will return the first 'n' elements of the array. 
// Test Data :
// console.log(first([7, 9, 0, -2]));
// console.log(first([],3));
// console.log(first([7, 9, 0, -2],3));
// console.log(first([7, 9, 0, -2],6));
// console.log(first([7, 9, 0, -2],-3));
// Expected Output :
// 7
// []
// [7, 9, 0]
// [7, 9, 0, -2]
// []


// 4. Write a JavaScript function to get the last element of an array. Passing a parameter 'n' will return the last 'n' elements of the array. 
// Test Data :
// console.log(last([7, 9, 0, -2]));
// console.log(last([7, 9, 0, -2],3));
// console.log(last([7, 9, 0, -2],6));
// Expected Output :
// -2
// [9, 0, -2]
// [7, 9, 0, -2]


// 5. Write a simple JavaScript program to join all elements of the following array into a string. 
// Sample array : myColor = ["Red", "Green", "White", "Black"];
// Expected Output :
// "Red,Green,White,Black"
// "Red,Green,White,Black"
// "Red+Green+White+Black"


// 6. Write a JavaScript program which accept a number as input and insert dashes (-) between each two even numbers. For example if you accept 025468 the output should be 0-254-6-8. 


// 7. Write a JavaScript program to sort the items of an array. 
// Sample array : var arr1 = [ 3, 8, 7, 6, 5, -4, 3, 2, 1 ];
// Sample Output : -4,-3,1,2,3,5,6,7,8


// 8. Write a JavaScript program to find the most frequent item of an array. 
// Sample array : var arr1=[3, 'a', 'a', 'a', 2, 3, 'a', 3, 'a', 2, 4, 9, 3];
// Sample Output : a ( 5 times )


// 9. Write a JavaScript program which accept a string as input and swap the case of each character. For example if you input 'The Quick Brown Fox' the output should be 'tHE qUICK bROWN fOX'. 


// 10. Write a JavaScript program which prints the elements of the following array. 
// Note : Use nested for loops.
// Sample array : var a = [[1, 2, 1, 24], [8, 11, 9, 4], [7, 0, 7, 27], [7, 4, 28, 14], [3, 10, 26, 7]];
// Sample Output :
// "row 0"
// " 1"
// " 2"
// " 1"
// " 24"
// "row 1"
// ------
// ------


// 11. Write a JavaScript program to find the sum of squares of a numeric vector. 


// 12. Write a JavaScript program to compute the sum and product of an array of integers. 


// 13. Write a JavaScript program to add items in an blank array and display the items. 
// Sample Screen :
// add elements in an blank array


// 14. Write a JavaScript program to remove duplicate items from an array (ignore case sensitivity). 


// 15. We have the following arrays : 
// color = ["Blue ", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow "];
// o = ["th","st","nd","rd"]
// Write a JavaScript program to display the colors in the following way :
// "1st choice is Blue ."
// "2nd choice is Green."
// "3rd choice is Red."
// - - - - - - - - - - - - -
// Note : Use ordinal numbers to tell their position.


// 16. Find the leap years in a given range of years. 


// 17. Write a JavaScript program to shuffle an array. 


// 18. Write a JavaScript program to perform a binary search. 
// Note : A binary search or half-interval search algorithm finds the position of a specified input value within an array sorted by key value.
// Sample array :
// var items = [1, 2, 3, 4, 5, 7, 8, 9];
// Expected Output :
// console.log(binary_Search(items, 1)); //0
// console.log(binary_Search(items, 5)); //4


// 19. There are two arrays with individual values, write a JavaScript program to compute the sum of each individual index value from the given arrays. 
// Sample array :
// array1 = [1,0,2,3,4];
// array2 = [3,5,6,7,8,13];
// Expected Output :
// [4, 5, 8, 10, 12, 13]


// 20. Write a JavaScript program to find duplicate values in a JavaScript array. 


// 21. Write a JavaScript program to flatten a nested (any depth) array. If you pass shallow, the array will only be flattened a single level. 
// Sample Data :
// console.log(flatten([1, [2], [3, [[4]]],[5,6]]));
// [1, 2, 3, 4, 5, 6]
// console.log(flatten([1, [2], [3, [[4]]],[5,6]], true));
// [1, 2, 3, [[4]], 5, 6]


// 22. Write a JavaScript program to compute the union of two arrays. 
// Sample Data :
// console.log(union([1, 2, 3], [100, 2, 1, 10]));
// [1, 2, 3, 10, 100]


// 23. Write a JavaScript function to find the difference of two arrays. 
// Test Data :
// console.log(difference([1, 2, 3], [100, 2, 1, 10]));
// ["3", "10", "100"]
// console.log(difference([1, 2, 3, 4, 5], [1, [2], [3, [[4]]],[5,6]]));
// ["6"]
// console.log(difference([1, 2, 3], [100, 2, 1, 10]));
// ["3", "10", "100"]


// 24. Write a JavaScript function to remove. 'null', '0', '""', 'false', 'undefined' and 'NaN' values from an array. 
// Sample array : [NaN, 0, 15, false, -22, '',undefined, 47, null]
// Expected result : [15, -22, 47]


// 25. Write a JavaScript function to sort the following array of objects by title value. 
// Sample object :

// var library = [ 
//    { author: 'Bill Gates', title: 'The Road Ahead', libraryID: 1254},
//    { author: 'Steve Jobs', title: 'Walter Isaacson', libraryID: 4264},
//    { author: 'Suzanne Collins', title: 'Mockingjay: The Final Book of The Hunger Games', libraryID: 3245}
//    ];

// Expected result :

// [[object Object] {
//   author: "Suzanne Collins",
//   libraryID: 3245,
//   title:"Mockingjay:The Final Book of The Hunger Games"
// }, [object Object] {
//   author: "Bill Gates",
//   libraryID: 1254,
//   title: "The Road Ahead"
// }, [object Object] {
//   author: "Steve Jobs",
//   libraryID: 4264,
//   title: "Walter Isaacson"
// }]



// 26. Write a JavaScript program to find a pair of elements (indices of the two numbers) from an given array whose sum equals a specific target number. 

// Input: numbers= [10,20,10,40,50,60,70], target=50
// Output: 2, 3



// 27. Write a JavaScript function to retrieve the value of a given property from all elements in an array. 
// Sample array : [NaN, 0, 15, false, -22, '',undefined, 47, null]
// Expected result : [15, -22, 47]


// 28. Write a JavaScript function to find the longest common starting substring in a set of strings. 

// Sample array : console.log(longest_common_starting_substring(['go', 'google']));
// Expected result : "go"



// 29. Write a JavaScript function to fill an array with values (numeric, string with one character) on supplied bounds. 

// Test Data :
// console.log(num_string_range('a', "z", 2));
// ["a", "c", "e", "g", "i", "k", "m", "o", "q", "s", "u", "w", "y"]



// 30. Write a JavaScript function to merge two arrays and removes all duplicates elements. 

// Test data :
// var array1 = [1, 2, 3];
// var array2 = [2, 30, 1];
// console.log(merge_array(array1, array2));
// [3, 2, 30, 1]



// 31. Write a JavaScript function to remove a specific element from an array. 

// Test data :
// console.log(remove_array_element([2, 5, 9, 6], 5));
// [2, 9, 6]


// 32. Write a JavaScript function to find an array contains a specific element. 

// Test data :
// arr = [2, 5, 9, 6];
// console.log(contains(arr, 5));
// [True]


// 33. Write a JavaScript script to empty an array keeping the original. 



// 34. Write a JavaScript function to get nth largest element from an unsorted array. 

// Test Data :
// console.log(nthlargest([ 43, 56, 23, 89, 88, 90, 99, 652], 4));
// 89



// 35. Write a JavaScript function to get a random item from an array. 



// 36. Write a JavaScript function to create a specified number of elements with pre-filled numeric value array. 

// Test Data :
// console.log(array_filled(6, 0));
// [0, 0, 0, 0, 0, 0]
// console.log(array_filled(4, 11));
// [11, 11, 11, 11]



// 37. Write a JavaScript function to create a specified number of elements with pre-filled string value array. 

// Test Data :
// console.log(array_filled(3, 'default value'));
// ["default value", "default value", "default value"]
// console.log(array_filled(4, 'password'));
// ["password", "password", "password", "password"]


// 38. Write a JavaScript function to move an array element from one position to another. 

// Test Data :
// console.log(move([10, 20, 30, 40, 50], 0, 2));
// [20, 30, 10, 40, 50]
// console.log(move([10, 20, 30, 40, 50], -1, -2));
// [10, 20, 30, 50, 40]


// 39. Write a JavaScript function to filter false, null, 0 and blank values from an array. 

// Test Data :
// console.log(filter_array_values([58, '', 'abcd', true, null, false, 0]));
// [58, "abcd", true]


// 40. Write a JavaScript function to generate an array of specified length, filled with integer numbers, increase by one from starting position. 

// Test Data :
// console.log(array_range(1, 4));
// [1, 2, 3, 4]
// console.log(array_range(-6, 4));
// [-6, -5, -4, -3]


// 41. Write a JavaScript function to generate an array between two integers of 1 step length. 

// Test Data :
// console.log(rangeBetwee(4, 7));
// [4, 5, 6, 7]
// console.log(rangeBetwee(-4, 7));
// [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]


// 42. Write a JavaScript function to find the unique elements from two arrays. 

// Test Data :
// console.log(difference([1, 2, 3], [100, 2, 1, 10]));
// ["1", "2", "3", "10", "100"]
// console.log(difference([1, 2, 3, 4, 5], [1, [2], [3, [[4]]],[5,6]]));
// ["1", "2", "3", "4", "5", "6"]
// console.log(difference([1, 2, 3], [100, 2, 1, 10]));
// ["1", "2", "3", "10", "100"]






Basics.html  1. Write a JavaScript program to display the current day and time in the following format.  
 Sample Output : Today is : Tuesday.
 Current time is : 10 PM : 30 : 38

HTML
<!DOCTYPE html>
  <html>
  <head>
  <meta charset="utf-8">
  <title>JavaScript current day and time</title>
  </head>
  <body></body>
</html>

JS
var today = new Date();
  var day = today.getDay();
  var daylist = ["Sunday","Monday","Tuesday","Wednesday ","Thursday","Friday","Saturday"];
  console.log("Today is : " + daylist[day] + ".");
  var hour = today.getHours();
  var minute = today.getMinutes();
  var second = today.getSeconds();
  var prepand = (hour >= 12)? " PM ":" AM ";
  hour = (hour >= 12)? hour - 12: hour;
  if (hour===0 && prepand===' PM ') 
  { 
  if (minute===0 && second===0)
  { 
  hour=12;
  prepand=' Noon';
  } 
  else
  { 
  hour=12;
  prepand=' PM';
  } 
  } 
  if (hour===0 && prepand===' AM ') 
  { 
  if (minute===0 && second===0)
  { 
  hour=12;
  prepand=' Midnight';
  } 
  else
  { 
  hour=12;
  prepand=' AM';
  } 
  } 
console.log("Current Time : "+hour + prepand + " : " + minute + " : " + second);


 2. Write a JavaScript program to print the contents of the current window.  

HTML Code:
<!DOCTYPE HTML>
<html>
<head>
<meta charset=utf-8 />
<title>Print the current page.</title>
</head>
<body>
<p>Click the button to print the current page.</p>
<button onclick="print_current_page()">Print this page</button>
</body>
</html>

JavaScript Code:
function print_current_page()
{
window.print();
}

 3. Write a JavaScript program to get the current date.  
 Expected Output :
 mm-dd-yyyy, mm/dd/yyyy or dd-mm-yyyy, dd/mm/yyyy

HTML Code:
<!DOCTYPE html>
  <html>
  <head>
  <meta charset="utf-8">
  <title>Write a JavaScript program to get the current date.</title>
  </head>
  <body>
  </body>
  </html>

JavaScript Code:
var today = new Date();
var dd = today.getDate();

var mm = today.getMonth()+1; 
var yyyy = today.getFullYear();
if(dd<10) 
{
    dd='0'+dd;
} 

if(mm<10) 
{
    mm='0'+mm;
} 
today = mm+'-'+dd+'-'+yyyy;
console.log(today);
today = mm+'/'+dd+'/'+yyyy;
console.log(today);
today = dd+'-'+mm+'-'+yyyy;
console.log(today);
today = dd+'/'+mm+'/'+yyyy;
console.log(today);

 4. Write a JavaScript program to find the area of a triangle where lengths of the three of its sides are 5, 6, 7.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
<meta charset=utf-8 />
<title>The area of a triangle</title>
</head>
<body>  
</body>
</html>

JavaScript Code:

var side1 = 5; 
var side2 = 6; 
var side3 = 7; 
var s = (side1 + side2 + side3)/2;
var area =  Math.sqrt(s*((s-side1)*(s-side2)*(s-side3)));
console.log(area);

 5. Write a JavaScript program to rotate the string 'w3resource' in right direction by periodically removing one letter from the end of the string and attaching it to the front.  

HTML Code:

<!DOCTYPE html>
  <html> 
  <head>
  <title>JavaScript basic animation</title>
  <script type="text/javascript">
  </script>
  </head> <body onload="animate_string('target')"
  <pre id="target">w3resource </pre>
  </body> 
  </html>
  
JavaScript Code:

function animate_string(id) 
{
    var element = document.getElementById(id);
    var textNode = element.childNodes[0];  assuming no other children
    var text = textNode.data;

setInterval(function () 
{
 text = text[text.length - 1] + text.substring(0, text.length - 1);
  textNode.data = text;
}, 100);
}

 6. Write a JavaScript program to determine whether a given year is a leap year in the Gregorian calendar.  

HTML Code:

<!DOCTYPE html>
<html>
<head>
<meta charset=utf-8 />
<title>Find Leap Year</title>
</head>
<body>
</body>
</html>


JavaScript Code:

function leapyear(year)
{
return (year % 100 === 0) ? (year % 400 === 0) : (year % 4 === 0);
}
console.log(leapyear(2016));
console.log(leapyear(2000));
console.log(leapyear(1700));
console.log(leapyear(1800));
console.log(leapyear(100));

 7. Write a JavaScript program to find 1st January is being a Sunday between 2014 and 2050.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
<meta charset=utf-8 />
<title>A Program to find 1st January is being a Sunday between 2014 and 2050.</title>
</head>
<body>
</body>
</html>


JavaScript Code:

console.log('--------------------');
for (var year = 2014; year <= 2050; year++)
    {
    var d = new Date(year, 0, 1);
    if ( d.getDay() === 0 )
        console.log("1st January is being a Sunday  "+year);
    }
console.log('--------------------');


 8. Write a JavaScript program where the program takes a random integer between 1 to 10, the user is then prompted to input a guess number. If the user input matches with guess number, the program will display a message "Good Work" otherwise display a message "Not matched".  
HTML Code:

<!DOCTYPE html>
<html>
<head>
<meta charset=utf-8 />
<title>Guess a number</title>
</head>
<body>
</body>
</html>


JavaScript Code:

 Get a random integer from 1 to 10 inclusive
 const num = Math.ceil(Math.random() * 10);
console.log(num);
 const gnum = prompt('Guess the number between 1 and 10 inclusive');
 if (gnum == num)
   console.log('Matched');
  else
   console.log('Not matched, the number was '+gnum);
   

 9. Write a JavaScript program to calculate days left until next Christmas.  
HTML Code:

<!DOCTYPE html>
  <html>
  <head>
  <meta charset=utf-8 />
  <title>Write a JavaScript program to calculate days left until next Christmas</title>
  </head>
  <body>
</body>
  </html>
  


JavaScript Code:

today=new Date();
var cmas=new Date(today.getFullYear(), 11, 25);
if (today.getMonth()==11 && today.getDate()>25) 
{
cmas.setFullYear(cmas.getFullYear()+1); 
}  
var one_day=1000*60*60*24;
console.log(Math.ceil((cmas.getTime()-today.getTime())/(one_day))+
" days left until Christmas!");

 10. Write a JavaScript program to calculate multiplication and division of two numbers (input from user).  
 Sample form :
 sample form

HTML Code:

<!DOCTYPE html>
<html> 
<head>
<meta charset=utf-8 />
<title>JavaScript program to calculate multiplication and division of two numbers </title>
<style type="text/css">
body {margin: 30px;}
</style> 
</head>
<body>
<form>
1st Number : <input type="text" id="firstNumber" /><br>
2nd Number: <input type="text" id="secondNumber" /><br>
<input type="button" onClick="multiplyBy()" Value="Multiply" />
<input type="button" onClick="divideBy()" Value="Divide" />
</form>
<p>The Result is : <br>
<span id = "result"></span>
</p>
</body>
</html>


JavaScript Code:

function multiplyBy()
{
        num1 = document.getElementById("firstNumber").value;
        num2 = document.getElementById("secondNumber").value;
        document.getElementById("result").innerHTML = num1 * num2;
}

function divideBy() 
{ 
        num1 = document.getElementById("firstNumber").value;
        num2 = document.getElementById("secondNumber").value;
document.getElementById("result").innerHTML = num1 / num2;
}


11. Write a JavaScript program to convert temperatures to and from Celsius, Fahrenheit.  
[ Formula : c/5 = (f-32)/9 [ where c = temperature in Celsius and f = temperature in Fahrenheit ]
Expected Output :
60°C is 140 °F
45°F is 7.222222222222222°C

HTML Code:

<!DOCTYPE html>
  <html>
  <head>
  <meta charset="utf-8">
  <title>Write a JavaScript program to convert temperatures to and from celsius, fahrenheit</title>
  </head>
  <body>
</body>
  </html>
  


JavaScript Code:

function cToF(celsius) 
{
  var cTemp = celsius;
  var cToFahr = cTemp * 9 / 5 + 32;
  var message = cTemp+'\xB0C is ' + cToFahr + ' \xB0F.';
    console.log(message);
}

function fToC(fahrenheit) 
{
  var fTemp = fahrenheit;
  var fToCel = (fTemp - 32) * 5 / 9;
  var message = fTemp+'\xB0F is ' + fToCel + '\xB0C.';
    console.log(message);
} 
cToF(60);
fToC(45);


 12. Write a JavaScript program to get the website URL (loading page).  
HTML Code:

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Write a JavaScript program to get the website URL (loading page)</title>
</head>
<body>
</body>
</html>


JavaScript Code:

//Write a JavaScript program to get the website URL (loading page)
console.log(document.URL);

 13. Write a JavaScript exercise to create a variable using a user-defined name.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Create a variable using a user-defined name</title>
</head>
<body>

</body>
</html>


JavaScript Code:

var var_name = 'abcd';
var n = 120;
this[var_name] = n;
console.log(this[var_name])

 14. Write a JavaScript exercise to get the extension of a filename.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>The extension of a filename.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

filename = "system.php"
console.log(filename.split('.').pop());
filename = "abc.js"
console.log(filename.split('.').pop());

 15. Write a JavaScript program to get the difference between a given number and 13, if the number is greater than 13 return double the absolute difference.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>The difference between a given number and 13, if the number is greater than 13 return double the absolute difference.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function difference(n)
 {
    if (n <= 13)
        return 13 - n;
    else
        return (n - 13) * 2;
 }
console.log(difference(32))
console.log(difference(11))

 16. Write a JavaScript program to compute the sum of the two given integers. If the two values are same, then returns triple their sum.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to compute the sum of the two given integers. If the two values are same, then return triple their sum</title>
</head>
<body>
</body>
</html>


JavaScript Code:

function sumTriple (x, y) {
  if (x == y) {
    return 3 * (x + y);
    } 
   else
   {
    return (x + y);
   }
 }
console.log(sumTriple(10, 20));
console.log(sumTriple(10, 10));


 17. Write a JavaScript program to compute the absolute difference between a specified number and 19. Returns triple their absolute difference if the specified number is greater than 19.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to compute the absolute difference between a specified number and 19.  Returns triple their absolute difference if the specified number is greater than 19.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function diff_num(n) {
  if (n <= 19) {
    return (19 - n);
    }
  else
    {
     return (n - 19) * 3;
    }
}

console.log(diff_num(12));
console.log(diff_num(19));
console.log(diff_num(22));

 18. Write a JavaScript program to check two given numbers and return true if one of the number is 50 or if their sum is 50.  

HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check two given numbers and return true if one of the number is 50 or if their sum is 50.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function test50(x, y) 
{
  return ((x == 50 || y == 50) || (x + y == 50));
}
console.log(test50(50, 50))
console.log(test50(20, 50))
console.log(test50(20, 20))
console.log(test50(20, 30))

 19. Write a JavaScript program to check whether a given integer is within 20 of 100 or 400.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check whether a given integer is within 20 of 100 or 400.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function testhundred(x) {
  return ((Math.abs(100 - x) <= 20) ||
   (Math.abs(400 - x) <= 20));
}

console.log(testhundred(10));
console.log(testhundred(90));
console.log(testhundred(99));
console.log(testhundred(199));
console.log(testhundred(200));


 20. Write a JavaScript program to check from two given integers, whether one is positive and another one is negative.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to  check from two given integers, whether one is positive and another one is negative.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function positive_negative(x, y)
{
  if ((x < 0 && y > 0) || x > 0 && y < 0) 
  {
    return true;
  }
  else 
  {
    return false;
  }
}
console.log(positive_negative(2, 2));
console.log(positive_negative(-2, 2));
console.log(positive_negative(2, -2));
console.log(positive_negative(-2, -2));

 21. Write a JavaScript program to create a new string adding "Py" in front of a given string. If the given string begins with "Py" then return the original string.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to create a new string adding “Py” in front of a given string.  If the given string begins with “Py” then return the original string.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function string_check(str1) {
  if (str1 === null || str1 === undefined || str1.substring(0, 2) === 'Py') 
  {
    return str1;
  }
  return "Py"+str1;
}

console.log(string_check("Python"));
console.log(string_check("thon"));

 22. Write a JavaScript program to remove a character at the specified position of a given string and return the new string.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to remove a character at the specified position of a given string and return the new string.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function remove_character(str, char_pos) 
 {
  part1 = str.substring(0, char_pos);
  part2 = str.substring(char_pos + 1, str.length);
  return (part1 + part2);
 }

console.log(remove_character("Python",0));
console.log(remove_character("Python",3));
console.log(remove_character("Python",5));

 23. Write a JavaScript program to create a new string from a given string changing the position of first and last characters. The string length must be greater than or equal to 1.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to create a new string from a given string changing the position of first and last characters.</title>
</head>
<body>
</body>
</html>


JavaScript Code:

function first_last(str1) 
  {
  if (str1.length <= 1)
  {
    return str1;
  }
  mid_char = str1.substring(1, str1.length - 1);
  return (str1.charAt(str1.length - 1)) + mid_char + str1.charAt(0);
}
console.log(first_last('a'));
console.log(first_last('ab'));
console.log(first_last('abc'));

 24. Write a JavaScript program to create a new string from a given string with the first character of the given string added at the front and back.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to create a new string from a given string with the first character of the given string added at the front and back.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function front_back(str)
{
  first = str.substring(0,1);
  return first + str + first;
}
console.log(front_back('a'));
console.log(front_back('ab'));
console.log(front_back('abc'));

 25. Write a JavaScript program to check whether a given positive number is a multiple of 3 or a multiple of 7.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check whether a given positive number is a multiple of 3 or a multiple of 7. </title>
</head>
<body>

</body>
</html>


JavaScript Code:

function test37(x) 
{
  if (x % 3 == 0 || x % 7 == 0) 
  {
    return true;
  } 
  else {
    return false;
  }
}

console.log(test37(12));
console.log(test37(14));
console.log(test37(10));
console.log(test37(11));

 26. Write a JavaScript program to create a new string from a given string taking the last 3 characters and added at both the front and back. The string length must be 3 or more.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to create a new string from a given string taking the last 3 characters and added at both the front and back. The string length must be 3 or more.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function front_back3(str)
 {
  if (str.length>=3)
   {
   str_len = 3;
 
  back = str.substring(str.length-3);
   return back + str + back;
 }
   else
     return false;
 }
console.log(front_back3("abc"));
console.log(front_back3("ab"));
console.log(front_back3("abcd"));

 27. Write a JavaScript program to check whether a string starts with 'Java' and false otherwise.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check whether a string starts with 'Java' and false otherwise.</title>
</head>
<body>
</body>
</html>


JavaScript Code:

function start_spec_str(str)
{
  if (str.length < 4)
  {
    return false;
  }
  front = str.substring(0, 4);
  if (front == 'Java') 
  {
    return true;
  }
   else 
   {
    return false;
  }
}

console.log(start_spec_str("JavaScript"));
console.log(start_spec_str("Java"));
console.log(start_spec_str("Python"));

 28. Write a JavaScript program to check whether two given integer values are in the range 50..99 (inclusive). Return true if either of them are in the said range.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check whether two given integer values are in the range 50..99 (inclusive). Return true if either of them are in the said range.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function check_numbers(x, y) 
  {
  if ((x >= 50 && x <= 99) || (y >= 50 && y <= 99))
  {
    return true;
  } 
  else 
  {
    return false;
  }
}

console.log(check_numbers(12, 101));
console.log(check_numbers(52, 80));
console.log(check_numbers(15, 99));

 29. Write a JavaScript program to check whether three given integer values are in the range 50..99 (inclusive). Return true if one or more of them are in the said range.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check whether three given integer values are in the range 50..99 (inclusive). Return true if one or more of them are in the said range.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function check_three_nums(x, y, z) 
{
  return (x >= 50 && x <= 99) || (y >= 50 && y <= 99) || (z >= 50 && z <= 99);
}

console.log(check_three_nums(50, 90, 99));
console.log(check_three_nums(5, 9, 199));
console.log(check_three_nums(65, 89, 199));
console.log(check_three_nums(65, 9, 199));

 30. Write a JavaScript program to check whether a string "Script" presents at 5th (index 4) position in a given string, if "Script" presents in the string return the string without "Script" otherwise return the original one.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check whether a string “Script” presents at 5th (index 4) position in a given string, if “Script” presents in the string return the string without “Script” otherwise return the original one.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function check_script(str)
{
  if (str.length < 6) {
    return str;
  }
  let result_str = str;
    
  if (str.substring(10, 4) == 'Script') 
    {
    
   result_str = str.substring(0, 4) + str.substring(10,str.length);
      
  }
  return result_str;
}

console.log(check_script("JavaScript"));
console.log(check_script("CoffeeScript"));

 31. Write a JavaScript program to find the largest of three given integers.  

HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to find the largest of three given integers.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function max_of_three(x, y, z) 
 {
  max_val = 0;
  if (x > y)
  {
    max_val = x;
  } else
  {
    max_val = y;
  }
  if (z > max_val) 
  {
    max_val = z;
  }
  return max_val;
}

console.log(max_of_three(1,0,1));
console.log(max_of_three(0,-10,-20));
console.log(max_of_three(1000,510,440));


 32. Write a JavaScript program to find a value which is nearest to 100 from two different given integer values.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to find a value which is nearest to 100 from two different given integer values.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function near_100(x, y) {
  if (x != y)
  {
  x1 = Math.abs(x - 100);
  y1 = Math.abs(y - 100);

  if (x1 < y1)
  {
    return x;
  }
  if (y1 < x1)
  {
    return y;
  }
  return 0;
  }
  else
    return false;
}

console.log(near_100(90, 89));
console.log(near_100(-90, -89));
console.log(near_100(90, 90));

 33. Write a JavaScript program to check whether two numbers are in range 40..60 or in the range 70..100 inclusive.  

HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check whether two numbers are in range 40..60 or in the range 70..100 inclusive</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function numbers_ranges(x, y) {
  if ((x >= 40 && x <= 60 && y >= 40 && y <= 60) 
      || 
      (x >= 70 && x <= 100 && y >= 70 && y <= 100))
     {
    return true;
     } 
    else 
     {
    return false;
  }
}

console.log(numbers_ranges(44, 56));
console.log(numbers_ranges(70, 95));
console.log(numbers_ranges(50, 89));  


 34. Write a JavaScript program to find the larger number from the two given positive integers, the two numbers are in the range 40..60 inclusive.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to find the larger number from the two given positive integers, the two numbers  are in the range 40..60 inclusive.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function max_townums_range(x, y){ 
if( (x >= 40) && (x <= 60) && (y >= 40 && y <= 60) ){
if(x === y){
return "Numbers are the same";
}else if (x > y){
return x;
}else{
return y;
}
}else{
return "Numbers don't fit in range";
}
}

console.log(max_townums_range(45, 60));
console.log(max_townums_range(25, 60));
console.log(max_townums_range(45, 80));

 35. Write a program to check whether a specified character exists within the 2nd to 4th position in a given string.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check a given string contains 2 to 4 numbers of a specified character.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function check_char(str1, char)
 {
  ctr = 0;
  for (let i = 0; i < str1.length; i++)
  {
    if ((str1.charAt(i) == char) && (i >= 1 && i <= 3))
    {
        ctr=1;
        break;
    }
   }
   if (ctr==1) return true;
   return false;
}
console.log(check_char("Python", "y"));
console.log(check_char("JavaScript", "a"));
console.log(check_char("Console", "o"));
console.log(check_char("Console", "C"));
console.log(check_char("Console", "e"));
console.log(check_char("JavaScript", "S"));

 36. Write a JavaScript program to check whether the last digit of the three given positive integers is same.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check whether the last digit of the three given positive integers is same.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function last_digit(x, y, z)
{
  if ((x > 0) && y > 0 && z > 0)
    {
     return (x % 10 == y % 10 && y % 10 == z % 10 && x % 10 == z % 10);
   }
  else
    return false;
}

console.log(last_digit(20, 30, 400));
console.log(last_digit(-20, 30, 400));
console.log(last_digit(20, -30, 400));
console.log(last_digit(20, 30, -400));

 37. Write a JavaScript program to create new string with first 3 characters are in lower case from a given string. If the string length is less than 3 convert all the characters in upper case.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to create new string with first 3 characters are in lower case from a given string. If the string length is less than 3 convert all the characters in upper case.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function upper_lower(str) {
  if (str.length < 3) {
    return str.toUpperCase();
  }
  front_part = (str.substring(0, 3)).toLowerCase();
  back_part = str.substring(3, str.length);  
  return front_part + back_part;
}
console.log(upper_lower("Python"));
console.log(upper_lower("Py"));
console.log(upper_lower("JAVAScript"));

 38. Write a JavaScript program to check the total marks of a student in various examinations. The student will get A+ grade if the total marks are in the range 89..100 inclusive, if the examination is "Final-exam." the student will get A+ grade and total marks must be greater than or equal to 90. Return true if the student get A+ grade or false otherwise.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check the total marks of a student in various examinations</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function exam_status(totmarks,is_exam)
  {
  if (is_exam) {
    return totmarks >= 90;
  }
 return (totmarks >= 89 && totmarks <= 100);
 }

console.log(exam_status("78", " "));
console.log(exam_status("89", "true "));
console.log(exam_status("99", "true "));

39. Write a JavaScript program to compute the sum of the two given integers, If the sum is in the range 50..80 return 65 other wise return 80.  

HTML Code:
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to compute the sum of the two given integers, If the sum is in the range 50..80  return 65 other wise return 80.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function sortaSum(x, y) 
 {
  const sum_nums = x + y;
  if (sum_nums >= 50 && sum_nums <= 80) {
    return 65;
  }
  return 80;
}

console.log(sortaSum(30,20));
console.log(sortaSum(90,80));

 40. Write a JavaScript program to check from two given integers whether one of them is 8 or their sum or difference is 8.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Write a JavaScript program to check from two given integers whether one of them is 8 or their sum or difference is 8.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function check8(x, y) {
  if (x == 8 || y == 8) {
    return true;
  }

  if (x + y == 8 || Math.abs(x - y) == 8)
  {
    return true;
  }

  return false;
}

console.log(check8(7, 8));
console.log(check8(16, 8));
console.log(check8(24, 32));
console.log(check8(17, 18));

 41. Write a JavaScript program to check three given numbers, if the three numbers are same return 30 otherwise return 20 and if two numbers are same return 40.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check three given numbers, if the three numbers are same return 30 otherwise return 20 and if two numbers are same return 40.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function three_numbers(x, y, z) {
  if (x == y && y == z) {
    return 30;
  }

  if (x == y || y == z || z == x) {
    return 40;
  }

  return 20;
}
console.log(three_numbers(8, 8, 8));
console.log(three_numbers(8, 8, 18));
console.log(three_numbers(8, 7, 18));


 42. Write a JavaScript program to check whether three given numbers are increasing in strict mode or in soft mode.  
 Note: Strict mode -> 10, 15, 31 : Soft mode -> 24, 22, 31 or 22, 22, 31
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Write a JavaScript program to check whether three given numbers are increasing in strict mode or in soft mode.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function number_order(x, y, z ) {
  if ( y > x && z > y) 
  {
    return "strict mode";    
  }
  else if(z > y) 
   return "Soft mode";
  else
    return "Undefinded";
}

console.log(number_order(10,15,31));
console.log(number_order(24,22,31));
console.log(number_order(50,21,15));

 43. Write a JavaScript program to check from three given numbers (non negative integers) that two or all of them have the same rightmost digit.  

HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check from three  given numbers (non negative integers) that two  or all of them have the same rightmost digit.</title>
</head>
<body>
</body>
</html>


JavaScript Code:

function same_last_digit(p, q, r) {
    return (p % 10 === q % 10) ||
           (p % 10 === r % 10) ||
           (q % 10 === r % 10);
           
}

console.log(same_last_digit(22,32,42));
console.log(same_last_digit(102,302,2));
console.log(same_last_digit(20,22,45));

 44. Write a JavaScript program to check from three given integers that whether a number is greater than or equal to 20 and less than one of the others.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check from three given integers that whether a number is greater than or equal to 20 and less than one of the others.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function lessby20_others(x, y, z) 
{
return (x >= 20 && (x < y || x < z)) ||
(y >= 20 && (y < x || y < z)) ||
(z >= 20 && (z < y || z < x));
}
console.log(lessby20_others(23, 45, 10));
console.log(lessby20_others(23, 23, 10));
console.log(lessby20_others(21, 66, 75));

45. Write a JavaScript program to check two given integer values and return true if one of the number is 15 or if their sum or difference is 15.  

HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check two given integer values and return true if one of the number is 15 or if their sum or difference is 15.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function test_number(x, y) {
    return (x === 15 || y === 15 || x + y === 15 || Math.abs(x - y) === 15);
}

console.log(test_number(15, 9));
console.log(test_number(25, 15));
console.log(test_number(7, 8));
console.log(test_number(25, 10));
console.log(test_number(5, 9));
console.log(test_number(7, 9));
console.log(test_number(9, 25));

 46. Write a JavaScript program to check two given non-negative integers that whether one of the number (not both) is multiple of 7 or 11.  

HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check two given non-negative integers that whether one of the number (not both) is multiple of 7 or 11.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function valCheck (a, b) {
if (!((a % 7 == 0 || a % 11 == 0) && (b % 7 == 0 || b % 11 == 0))) {
return ((a % 7 == 0 || a % 11 == 0) || (b % 7 == 0 || b % 11 == 0));
}
else
return false;
}
console.log(valCheck(14, 21));
console.log(valCheck(14, 20));
console.log(valCheck(16, 20));

 47. Write a JavaScript program to check whether a given number is presents in the range 40..10000.  
 For example 40 presents in 40 and 4000

HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check whether a given number is presents in the range 40..10000. </title>
</head>
<body>

</body>
</html>


JavaScript Code:

function test_digit(x, y, n) 
  {    
    if (n < 40 || n > 10000)
      return false;
    else
      if (n >= x && n <= y)
        return true;
      else
        return false;
  }
console.log(test_digit(40, 4000, 45));  
console.log(test_digit(80, 320, 79));  
console.log(test_digit(89, 4000, 30));

 48. Write a JavaScript program to reverse a given string.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to reverse a given string.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function string_reverse(str) 
{
    return str.split("").reverse().join("");
}

console.log(string_reverse("w3resource"));
console.log(string_reverse("www"));
console.log(string_reverse("JavaScript"));

 49. Write a JavaScript program to replace every character in a given string with the character following it in the alphabet.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to replace every character in a given string with the character following it in the alphabet.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function string_reverse(str) 
function LetterChanges(text) {
//https://goo.gl/R8gn7u
var s = text.split('');
for (var i = 0; i < s.length; i++) {
// Caesar cipher
switch(s[i]) {
case ' ':
break;
case 'z':
s[i] = 'a';
break;
case 'Z': 
s[i] = 'A';
break;
default:
s[i] = String.fromCharCode(1 + s[i].charCodeAt(0));
}

// Upper-case vowels
switch(s[i]) {
case 'a': case 'e': case 'i': case 'o': case 'u':
s[i] = s[i].toUpperCase();
}
}
return s.join('');
}
console.log(LetterChanges("PYTHON"));
console.log(LetterChanges("W3R"));
console.log(LetterChanges("php"));

 50. Write a JavaScript program to capitalize the first letter of each word of a given string.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to capitalize the first letter of each word of a given string.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function capital_letter(str) 
{
    str = str.split(" ");

    for (var i = 0, x = str.length; i < x; i++) {
        str[i] = str[i][0].toUpperCase() + str[i].substr(1);
    }

    return str.join(" ");
}

console.log(capital_letter("Write a JavaScript program to capitalize the first letter of each word of a given string."))

 51. Write a JavaScript program to convert a given number to hours and minutes.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to convert a given number to hours and minutes.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function time_convert(num)
 { 
  var hours = Math.floor(num / 60);  
  var minutes = num % 60;
  return hours + ":" + minutes;         
}

console.log(time_convert(71));
console.log(time_convert(450));
console.log(time_convert(1441));

 52. Write a JavaScript program to convert the letters of a given string in alphabetical order.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to convert the letters of a given string  in alphabetical order.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function alphabet_Soup(str) { 

    return str.split("").sort().join("");
         
}

console.log(alphabet_Soup("Python"));

console.log(alphabet_Soup("Exercises"));


 53. Write a JavaScript program to check whether the characters a and b are separated by exactly 3 places anywhere (at least once) in a given string.  

HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check whether the characters a and b are separated by exactly 3 places anywhere (at least once) in a given string.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function ab_Check(str)
 {
    return (/a...b/).test(str) || (/b...a/).test(str);
 }

console.log(ab_Check("Chainsbreak"));
console.log(ab_Check("pane borrowed"));
console.log(ab_Check("abCheck"));

 54. Write a JavaScript program to count the number of vowels in a given string.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to count the number of vowels in a given string.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function vowel_Count(str)
{ 

  return str.replace(/[^aeiou]/g, "").length; 
}

console.log(vowel_Count("Python"));
console.log(vowel_Count("w3resource.com"));

 55. Write a JavaScript program to check whether a given string contains equal number of p's and t's.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>check whether a given string contains equal number of p's and t's</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function equal_pt(str)
{ 
  var str_p = str.replace(/[^p]/g, "");

  var str_t = str.replace(/[^t]/g, "");

  var p_num = str_p.length;
  var s_num = str_t.length;

  return p_num === s_num;
         
}
console.log(equal_pt("paatpss"));
console.log(equal_pt("paatps"));

 56. Write a JavaScript program to divide two positive numbers and return a string with properly formatted commas.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to divide two positive numbers and return a string with properly formatted commas.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function division_string(n1, n2) {
  
n1 = 80;
n2 = 6;

var div = Math.round(n1 / n2).toString(),
result_array = div.split("");

if (div >= 1000)
{
for (var i = div.length - 3; i > 0; i -= 3) 
{
result_array.splice(i, 0, ",");
}
result_array;
}
console.log(result_array);

 57. Write a JavaScript program to create a new string of specified copies (positive number) of a given string.  

HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to create a new string of specified copies of a given string.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function string_copies (str, n) 
{
  if (n < 0)
    return false;
  else
  return str.repeat(n);
}
console.log(string_copies("abc", 5));
console.log(string_copies("abc", 0));
console.log(string_copies("abc", -2));

 58. Write a JavaScript program to create a new string of 4 copies of the last 3 characters of a given original string. The length of the given string must be 3 and above.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to create a new string of 4 copies of the last 3 characters of a given original string. The length of the given string must be 3 and above.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function newstring(str)
{
  if (str.length >= 3) {
    result_str = str.substring(str.length - 3);
    return result_str + result_str + result_str + result_str;
  }
  else
    return false;
}
console.log(newstring("Python 3.0"));
console.log(newstring("JS"));
console.log(newstring("JavaScript"));


 59. Write a JavaScript program to extract the first half of a string of even length.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to  extract the first half of a string of even length.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function first_half (str) {
  if (str.length % 2 == 0) {
    return str.slice(0, str.length / 2);
  }
  return str;
}
console.log(first_half("Python"));  
console.log(first_half("JavaScript")); 
console.log(first_half("PHP"));

 60. Write a JavaScript program to create a new string without the first and last character of a given string.  

HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to create a new string without the first and last character of a given string.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function without_first_end(str) {
  return str.substring(1, str.length - 1);
}
console.log(without_first_end('JavaScript'));
console.log(without_first_end('JS'));
console.log(without_first_end('PHP'));

 61. Write a JavaScript program to concatenate two strings except their first character.  


 62. Write a JavaScript program to move last three character to the start of a given string. The string length must be greater or equal to three.  


 63. Write a JavaScript program to create a string using the middle three characters of a given string of odd length. The string length must be greater or equal to three.  


 64. Write a JavaScript program to concatenate two strings and return the result. If the length of the strings are not same then remove the characters from the longer string.  


 65. Write a JavaScript program to test whether a string end with "Script". The string length must be greater or equal to 6.  


 66. Write a JavaScript program to display the city name if the string begins with "Los" or "New" otherwise return blank.  


 67. Write a JavaScript program to create a new string from a given string, removing the first and last characters of the string if the first or last character are 'P'. Return the original string if the condition is not satisfied.  


 68. Write a JavaScript program to create a new string using the first and last n characters from a given sting. The string length must be greater or equal to n.  


 69. Write a JavaScript program to compute the sum of three elements of a given array of integers of length 3.  


 70. Write a JavaScript program to rotate the elements left of a given array of integers of length 3.  


 71. Write a JavaScript program to check whether 1 appears in first or last position of a given array of integers. The array length must be greater or equal to 1.  


 72. Write a JavaScript program to check whether the first and last elements are equal of a given array of integers length 3.  


 73. Write a JavaScript program to reverse the elements of a given array of integers length 3.  


 74. Write a JavaScript program to find the larger value between the first or last and set all the other elements with that value. Display the new array.  


 75. Write a JavaScript program to create a new array taking the middle elements of the two arrays of integer and each length 3.  


 76. Write a JavaScript program to create a new array taking the first and last elements from a given array of integers and length must be greater or equal to 1.  


 77. Write a JavaScript program to test whether an array of integers of length 2 contains 1 or a 3.  


 78. Write a JavaScript program to test whether an array of integers of length 2 does not contain 1 or a 3.  


 79. Write a JavaScript program to test whether a given array of integers contains 30 and 40 twice. The array length should be 0, 1, or 2.  


 80. Write a JavaScript program to swap the first and last elements of a given array of integers. The array length should be at least 1.  


 81. Write a JavaScript program to add two digits of a given positive integer of length two.  


 82. Write a JavaScript to add two positive integers without carry.  


 83. Write a JavaScript to find the longest string from a given array of strings.  


 84. Write a JavaScript to replace each character of a given string by the next one in the English alphabet.  
 Note: 'a' will be replace by 'b' or 'z' would be replaced by 'a'.


 85. Write a JavaScript code to divide a given array of positive integers into two parts. First element goes to first part, second element goes to second part, and third element goes to first part and so on. Now compute the sum of two parts and store into an array of size two.  


 86. Write a JavaScript program to find the types of a given angle.  

     Types of angles:
     Acute angle: An angle between 0 and 90 degrees.
     Right angle: An 90 degree angle.
     Obtuse angle: An angle between 90 and 180 degrees.
     Straight angle: A 180 degree angle.



 87. Write a JavaScript program to check whether two arrays of integers of same length are similar or not. The arrays will be similar if one array can be obtained from another array by swapping at most one pair of elements.  


 88. Write a JavaScript program to check whether two given integers are similar or not, if a given divisor divides both integers and it does not divide either.  


 89. Write a JavaScript program to check whether it is possible to replace $ in a given expression x $ y = z with one of the four signs +, -, * or / to obtain a correct expression.  
 For example x = 10, y = 30 and z = 300, we can replace $ with a multiple operator (*) to obtain x * y = z


 90. Write a JavaScript program to find the kth greatest element of a given array of integers  


 91. Write a JavaScript program to find the maximum possible sum of some of its k consecutive numbers (numbers that follow each other in order.) of a given array of positive integers. 


 92. Write a JavaScript program to find the maximal difference between any two adjacent elements of a given array of integers. 


 93. Write a JavaScript program to find the maximal difference among all possible pairs of a given array of integers. 


 94. Write a JavaScript program to find the number which appears most in a given array of integers. 


 95. Write a JavaScript program to replace all the numbers with a specified number of a given array of integers. 


 96. Write a JavaScript program to compute the sum of absolute differences of consecutive numbers of a given array of integers. 


 97. Write a JavaScript program to find the shortest possible string which can create a string to make it a palindrome by adding characters to the end of it. 


 98. Write a JavaScript program to switch case of the minimum possible number of letters to make a given string written in the upper case or in the lower case. 
 Fox example "Write" will be write and "PHp" will be "PHP"


 99. Write a JavaScript program to check whether it is possible to rearrange characters of a given string in such way that it will become equal to another given string. 


 100. Write a JavaScript program to check whether there is at least one element which occurs in two given sorted arrays of integers. 


 101. Write a JavaScript program to check whether a given string contains only Latin letters and no two uppercase and no two lowercase letters are in adjacent positions. 


 102. Write a JavaScript program to find the number of inversions of a given array of integers. 
 Note: Two elements of the array a stored at positions i and j form an inversion if a[i] > a[j] and i < j.


 103. Write a JavaScript program to find the maximal number from a given positive integer by deleting exactly one digit of the given number. 


 104. Write a JavaScript program to find two elements of the array such that their absolute difference is not greater than a given integer but is as close to the said integer. 


 105. Write a JavaScript program to find the number of times to replace a given number with the sum of its digits until it convert to a single digit number. 


 106. Write a JavaScript program to divide an integer by another integer as long as the result is an integer and return the result. 


 107. Write a JavaScript program to find the number of sorted pairs formed by its elements of a given array of integers such that one element in the pair is divisible by the other one. 
 For example - The output of [1, 3, 2] ->2 - (1,3), (1,2).
 The output of [2, 4, 6] -> 2 - (2,4), (2,6)
 The output of [2, 4, 16] -> 3 - (2,4), (2,16), (4,16)


 108. Write a JavaScript program to create the dot products of two given 3D vectors. 
 Note: The dot product is the sum of the products of the corresponding entries of the two sequences of numbers.


 109. Write a JavaScript program to sort an array of all prime numbers between 1 and a given integer. 


 110. Write a JavaScript program to find the number of even values in sequence before the first occurrence of a given number. 


 111. Write a JavaScript program to check a number from three given numbers where two numbers are equal, find the third one. 


 112. Write a JavaScript program to find the number of trailing zeros in the decimal representation of the factorial of a given number. 


 113. Write a JavaScript program to calculate the sum of n + n/2 + n/4 + n/8 + .... where n is a positive integer and all divisions are integer. 


 114. Write a JavaScript program to check whether a given string represents a correct sentence or not. A string is considered correct sentence if it starts with the capital letter and ends with a full stop (.). 


 115. Write a JavaScript program to check whether a matrix is a diagonal matrix or not. In linear algebra, a diagonal matrix is a matrix in which the entries outside the main diagonal are all zero (the diagonal from the upper left to the lower right). 
 Example:
 [1, 0, 0], [0, 2, 0], [0, 0, 3] ]) = true
 [1, 0, 0], [0, 2, 3], [0, 0, 3] ]) = false


 116. Write a JavaScript program to find all the possible options to replace the hash in a string (Consists of digits and one hash (#)) with a digit to produce an integer divisible by 3. 
 For a string "2*0", the output should be : ["210", "240", "270"]


 117. Write a JavaScript program to check whether a given matrix is an identity matrix. 
 Note: In linear algebra, the identity matrix, or sometimes ambiguously called a unit matrix, of size n is the n ? n square matrix with ones on the main diagonal and zeros elsewhere.
 [[1, 0, 0], [0, 1, 0], [0, 0, 1]] -> true
 [[1, 0, 0], [0, 1, 0], [1, 0, 1]] -> false


 118. Write a JavaScript program to check whether a given number is in a given range. 


 119. Write a JavaScript program to check whether a given integer has an increasing digits sequence. 


 120. Write a JavaScript program to check whether a point lies strictly inside a given circle. 
 Input:
 Center of the circle (x, y)
 Radius of circle: r
 Point inside a circle (a, b)


 121. Write a JavaScript program to check whether a given matrix is lower triangular or not. 
 Note: A square matrix is called lower triangular if all the entries above the main diagonal are zero.


 122. Write a JavaScript program to check whether a given array of integers represents either a strictly increasing or a strictly decreasing sequence. 


 123. Write a JavaScript program to find whether the members of a given array of integers is a permutation of numbers from 1 to a given integer. 


 124. Write a JavaScript program to create the value of NOR of two given booleans. 
 Note: In boolean logic, logical nor or joint denial is a truth-functional operator which produces a result that is the negation of logical or. That is, a sentence of the form (p NOR q) is true precisely when neither p nor q is true - i.e. when both of p and q are false
 Sample Example:
 For x = true and y = false, the output should be logical_Nor(x, y) = false; For x = false and y = false, the output should be logical_Nor(x, y) = true.


 125. Write a JavaScript program to find the longest string from a given array. 


 126. Write a JavaScript program to get the largest even number from an array of integers. 


 127. Write a JavaScript program to reverse the order of the bits in a given integer. 
 56 -> 111000 after reverse 7 -> 111
 234 -> 11101010 after reverse 87 -> 1010111


 128. Write a JavaScript program to find the smallest round number that is not less than a given value. 
 Note: A round number is informally considered to be an integer that ends with one or more zeros.[3] So, 590 is rounder than 592, but 590 is less round than 600.


 129. Write a JavaScript program to find the smallest prime number strictly greater than a given number. 


 130. Write a JavaScript program to find the number of even digits in a given integer. 


 131. Write a JavaScript program to create an array of prefix sums of the given array. 
 In computer science, the prefix sum, cumulative sum, inclusive scan, or simply scan of a sequence of numbers x0, x1, x2, ... is a second sequence of numbers y0, y1, y2, ..., the sums of prefixes of the input sequence:
 y0 = x0
 y1 = x0 + x1
 y2 = x0 + x1+ x2
 ...


 132. Write a JavaScript program to find all distinct prime factors of a given integer. 


 133. Write a JavaScript program to check whether a given fraction is proper or not. 
 Note: There are two types of common fractions, proper or improper. When the numerator and the denominator are both positive, the fraction is called proper if the numerator is less than the denominator, and improper otherwise.


 134. Write a JavaScript program to change the characters (lower case) in a string where a turns into z, b turns into y, c turns into x, ..., n turns into m, m turns into n, ..., z turns into a. 


 135. Write a JavaScript program to remove all characters from a given string that appear more than once. 


 136. Write a JavaScript program to replace the first digit in a string (should contains at least digit) with $ character. 


 137. Write a JavaScript program to test whether a given integer is greater than 15 return the given number, otherwise return 15. 


 138. Write a JavaScript program to reverse the bits of a given 16 bits unsigned short integer. 


 139. Write a JavaScript program to find the position of a rightmost round number in an array of integers. Returns 0 if there are no round number.  
 Note: A round number is informally considered to be an integer that ends with one or more zeros.


 140. Write a JavaScript program to check whether all the digits in a given number are the same or not.  


 141. Write a JavaScript program to find the number of elements which presents in both of the given arrays.  


 142. Write a JavaScript program to simplify a given absolute path for a file in Unix-style.  


 143. Write a JavaScript program to sort the strings of a given array of strings in the order of increasing lengths.  
 Note: Do not change the order if the lengths of two string are same.


 144. Write a JavaScript program to break an address of an url and put it's part into an array.  
 Note: url structure : :.org[/] and there may be no part in the address.


 145. Write a JavaScript program to find the maximum integer n such that 1 + 2 + ... + n <= a given integer.  


 146. Write a JavaScript program to compute the sum of cubes of all integer from 1 to a given integer.  


 147. Write a JavaScript program to compute the sum of all digits that occur in a given string.  


 148. Write a JavaScript program to swap two halves of a given array of integers of even length.  


 149. Write a JavaScript program to change the capitalization of all letters in a given string.  


 150. Write a JavaScript program to swap pairs of adjacent digits of a given integer of even length.  




Conditional Statements and Loops.html // 1. Write a JavaScript program that accept two integers and display the larger. 


// 2. Write a JavaScript conditional statement to find the sign of product of three numbers. Display an alert box with the specified sign. 
// Sample numbers : 3, -7, 2
// Output : The sign is -


// 3. Write a JavaScript conditional statement to sort three numbers. Display an alert box to show the result. 
// Sample numbers : 0, -1, 4
// Output : 4, 0, -1


// 4. Write a JavaScript conditional statement to find the largest of five numbers. Display an alert box to show the result. 
// Sample numbers : -5, -2, -6, 0, -1
// Output : 0


// 5. Write a JavaScript for loop that will iterate from 0 to 15. For each iteration, it will check if the current number is odd or even, and display a message to the screen. 
// Sample Output :
// "0 is even"
// "1 is odd"
// "2 is even"
// ----------
// ----------


// 6. Write a JavaScript program which compute, the average marks of the following students Then, this average is used to determine the corresponding grade. 
// Student Name 	Marks
// David 	80
// Vinoth 	77
// Divya 	88
// Ishitha 	95
// Thomas 	68

// The grades are computed as follows :
// Range 	Grade
// <60 	F
// <70 	D
// <80 	C
// <90 	B
// <100 	A



// 7. Write a JavaScript program which iterates the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz". 


// 8. According to Wikipedia a happy number is defined by the following process :
// "Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers (or sad numbers)".
// Write a JavaScript program to find and print the first 5 happy numbers. 


// 9. Write a JavaScript program to find the armstrong numbers of 3 digits. 
// Note : An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself. For example, 371 is an Armstrong number since 3**3 + 7**3 + 1**3 = 371.


// 10. Write a JavaScript program to construct the following pattern, using a nested for loop. 

// *  
// * *  
// * * *  
// * * * *  
// * * * * *  



// 11. Write a JavaScript program to compute the greatest common divisor (GCD) of two positive integers. 


// 12. Write a JavaScript program to sum the multiples of 3 and 5 under 1000. 




Date.html // 1. Write a JavaScript function to check whether an `input` is a date object or not. 

// Test Data :
// console.log(is_date("October 13, 2014 11:13:00"));
// console.log(is_date(new Date(86400000)));
// console.log(is_date(new Date(99,5,24,11,33,30,0)));
// console.log(is_date([1, 2, 4, 0]));
// Output :
// false
// true
// true
// false



// 2. Write a JavaScript function to get the current date. 

// Note : Pass a separator as an argument.
// Test Data :
// console.log(curday('/'));
// console.log(curday('-'));
// Output :
// "11/13/2014"
// "11-13-2014"



// 3. Write a JavaScript function to get the number of days in a month. 

// Test Data :
// console.log(getDaysInMonth(1, 2012));
// console.log(getDaysInMonth(2, 2012));
// console.log(getDaysInMonth(9, 2012));
// console.log(getDaysInMonth(12, 2012));
// Output :
// 31
// 29
// 30
// 31



// 4. Write a JavaScript function to get the month name from a particular date. 

// Test Data :
// console.log(month_name(new Date("10/11/2009")));
// console.log(month_name(new Date("11/13/2014")));
// Output :
// "October"
// "November"



// 5. Write a JavaScript function to compare dates (i.e. greater than, less than or equal to). 

// Test Data :
// console.log(compare_dates(new Date('11/14/2013 00:00'), new Date('11/14/2013 00:00')));
// console.log(compare_dates(new Date('11/14/2013 00:01'), new Date('11/14/2013 00:00')));
// console.log(compare_dates(new Date('11/14/2013 00:00'), new Date('11/14/2013 00:01')));
// Output :
// "Date1 = Date2"
// "Date1 > Date2"
// "Date2 > Date1"



// 6. Write a JavaScript function to add specified minutes to a Date object. 

// Test Data :
// console.log(add_minutes(new Date(2014,10,2), 30).toString());
// Output :
// "Sun Nov 02 2014 00:30:00 GMT+0530 (India Standard Time)"



// 7. Write a JavaScript function to test whether a date is a weekend. 

// Note : Use standard Saturday/Sunday definition of a weekend.
// Test Data :
// console.log(is_weekend('Nov 15, 2014'));
// console.log(is_weekend('Nov 16, 2014'));
// console.log(is_weekend('Nov 17, 2014'));
// Output :
// "weekend"
// "weekend"
// undefined



// 8. Write a JavaScript function to get difference between two dates in days. 

// Test Data :
// console.log(date_diff_indays('04/02/2014', '11/04/2014'));
// console.log(date_diff_indays('12/02/2014', '11/04/2014'));
// Output :
// 216
// -28



// 9. Write a JavaScript function to get the last day of a month. 

// Test Data :
// console.log(lastday(2014,0));
// console.log(lastday(2014,1));
// console.log(lastday(2014,11));
// Output :
// 31
// 28
// 31



// 10. Write a JavaScript function to calculate 'yesterday day'. 

// Test Data :
// console.log(yesterday('Nov 15, 2014'));
// console.log(yesterday('Nov 16, 2015'));
// console.log(yesterday('Nov 17, 2016'));
// Output :
// "Fri Nov 14 2014 00:00:00 GMT+0530 (India Standard Time)"
// "Sun Nov 15 2015 00:00:00 GMT+0530 (India Standard Time)"
// "Wed Nov 16 2016 00:00:00 GMT+0530 (India Standard Time)"



// 11. Write a JavaScript function to get the maximum date from an array of dates. 

// Test Data :
// console.log(max_date(['2015/02/01', '2015/02/02', '2015/01/03']));
// Output :
// "2015/02/02"



// 12. Write a JavaScript function to get the minimum date from an array of dates. 

// Test Data :
// console.log(min_date(['2015/02/01', '2015/02/02', '2015/01/03']));
// Output :
// "2015/01/03"



// 13. Write a JavaScript function that will return the number of minutes in hours and minutes. 

// Test Data :
// console.log(timeConvert(200));
// Output :
// "200 minutes = 3 hour(s) and 20 minute(s)."



// 14. Write a JavaScript function to get the amount of days of a year. 

// Test Data :
// console.log(days_of_a_year(2015));
// 365
// console.log(days_of_a_year(2016));
// 366



// 15. Write a JavaScript function to get the quarter (1 to 4) of the year. 

// Test Data :
// console.log(quarter_of_the_year(new Date(2015, 1, 21)));
// 2
// console.log(quarter_of_the_year(new Date(2015, 10, 18)));
// 4



// 16. Write a JavaScript function to count the number of days passed since beginning of the year. 

// Test Data :
// console.log(days_passed(new Date(2015, 0, 15)));
// 15
// console.log(days_passed(new Date(2015, 11, 14)));
// 348



// 17. Write a JavaScript function to convert a Unix timestamp to time. 

// Test Data :
// console.log(days_passed(new Date(2015, 0, 15)));
// 15
// console.log(days_passed(new Date(2015, 11, 14)));
// 348



// 18. Write a JavaScript program to calculate age. 

// Test Data :
// console.log(calculate_age(new Date(1982, 11, 4)));
// 32
// console.log(calculate_age(new Date(1962, 1, 1)));
// 53



// 19. Write a JavaScript function to get the day of the month, 2 digits with leading zeros. 
// Test Data :
// d= new Date(2015, 10, 1);
// console.log(day_of_the_month(d));
// "01"



// 20. Write a JavaScript function to get a textual representation of a day (three letters, Mon through Sun). 
// Test Data :
// dt = new Date(2015, 10, 1);
// console.log(short_Days(dt));
// "Sun"



// 21. Write a JavaScript function to get a full textual representation of the day of the week (Sunday through Saturday). 
// Test Data :
// dt = new Date(2015, 10, 1);
// console.log(long_Days(dt));
// "Sunday"



// 22. Write a JavaScript function to get ISO-8601 numeric representation of the day of the week (1 (for Monday) to 7 (for Sunday)). 
// Test Data :
// dt = new Date(2015, 10, 1);
// console.log(ISO_numeric_date(dt));
// 7



// 23. Write a JavaScript function to get English ordinal suffix for the day of the month, 2 characters (st, nd, rd or th.). 
// Test Data :
// dt = new Date(2015, 10, 1);
// console.log(english_ordinal_suffix(dt));
// "1st"



// 24. Write a JavaScript function to get ISO-8601 week number of year, weeks starting on Monday. 
// Example : 42 (the 42nd week in the year)
// Test Data :
// dt = new Date(2015, 10, 1);
// console.log(ISO8601_week_no(dt));
// 44



// 25. Write a JavaScript function to get a full textual representation of a month, such as January or June. 
// Test Data :
// dt = new Date(2015, 10, 1);
// console.log(full_month(dt));
// "November"



// 26. Write a JavaScript function to get a numeric representation of a month, with leading zeros (01 through 12). 
// Test Data :
// dt = new Date(2015, 10, 1);
// console.log(numeric_month(dt));
// "11"



// 27. Write a JavaScript function to get a short textual representation of a month, three letters (Jan through Dec). 
// Test Data :
// dt = new Date(2015, 10, 1);
// console.log(short_months(dt));
// "Nov"



// 28. Write a JavaScript function to get a full numeric representation of a year (4 digits). 
// Test Data :
// dt = new Date(2015, 10, 1);
// console.log(full_year(dt));
// 2015



// 29. Write a JavaScript function to get a two digit representation of a year. 
// Examples : 79 or 04
// Test Data :
// dt = new Date(1989, 10, 1);
// console.log(sort_year(dt));
// "89"



// 30. Write a JavaScript function to get lowercase Ante meridiem and Post meridiem. 


// 31. Write a JavaScript function to get uppercase Ante meridiem and Post meridiem. 



// 32. Write a JavaScript function to swatch Internet time (000 through 999). 
// Test Data :
// dt = new Date(1989, 10, 1);
// console.log(internet_time(dt));
// 812



// 33. Write a JavaScript function to get 12-hour format of an hour with leading zeros. 
// Test Data :
// dt = new Date(1989, 10, 1);
// console.log(hours_with_zeroes(dt));
// "12"



// 34. Write a JavaScript function to get 24-hour format of an hour without leading zeros. 
// Test Data :
// dt = new Date(1989, 10, 1);
// console.log(hours_without_zeroes(dt));
// 0



// 35. Write a JavaScript function to get minutes with leading zeros (00 to 59). 
// Test Data :
// dt = new Date(1989, 10, 1);
// console.log(minutes_with_leading_zeros(dt));
// "00"



// 36. Write a JavaScript function to get seconds with leading zeros (00 through 59). 
// Test Data :
// dt = new Date(1989, 10, 1);
// console.log(seconds_with_leading_zeros(dt));
// "00"



// 37. Write a JavaScript function to get Timezone. 
// Test Data :
// dt = new Date();
// console.log(seconds_with_leading_zeros(dt));
// "India Standard Time"


// 38. Write a JavaScript function to find whether or not the date is in daylights savings time. 
// Test Data :
// dt = new Date();
// console.log(daylights_savings(dt));
// 1



// 39. Write a JavaScript function to get difference to Greenwich time (GMT) in hours. 
// Test Data :
// dt = new Date();
// console.log(diff_to_GMT(dt));
// "+05.500"



// 40. Write a JavaScript function to get timezone offset in seconds. 
// Note : The offset for timezones west of UTC is always negative, and for those east of UTC is always positive.
// Test Data :
// dt = new Date();
// console.log(timezone_offset_in_seconds(dt));
// 19800



// 41. Write a JavaScript function to add specified years to a date. 
// Test Data :
// dt = new Date(2014,10,2);
// console.log(add_years(dt, 10).toString());
// Output :
// "Sat Nov 02 2024 00:00:00 GMT+0530 (India Standard Time)"



// 42. Write a JavaScript function to add specified weeks to a date. 
// Test Data :
// dt = new Date(2014,10,2);
// console.log(add_weeks(dt, 10).toString());
// Output :
// "Sun Jan 11 2015 00:00:00 GMT+0530 (India Standard Time)"



// 43. Write a JavaScript function to add specified months to a date. 
// Test Data :
// dt = new Date(2014,10,2);
// console.log(add_months(dt, 10).toString());
// Output :
// "Wed Sep 02 2015 00:00:00 GMT+0530 (India Standard Time)"



// 44. Write a JavaScript function to get time differences in minutes between two dates. 
// Test Data :
// dt1 = new Date("October 13, 2014 11:11:00");
// dt2 = new Date("October 13, 2014 11:13:00");
// console.log(diff_minutes(dt1, dt2));
// 2



// 45. Write a JavaScript function to get time differences in hours between two dates. 
// Test Data :
// dt1 = new Date("October 13, 2014 08:11:00");
// dt2 = new Date("October 13, 2014 11:13:00");
// console.log(diff_hours(dt1, dt2));
// 3



// 46. Write a JavaScript function to get time differences in days between two dates. 
// Test Data :
// dt1 = new Date("October 13, 2014 08:11:00");
// dt2 = new Date("October 19, 2014 11:13:00");
// console.log(diff_days(dt1, dt2));
// 6



// 47. Write a JavaScript function to get time differences in weeks between two dates. 
// Test Data :
// dt1 = new Date("June 13, 2014 08:11:00");
// dt2 = new Date("October 19, 2014 11:13:00");
// console.log(diff_weeks(dt1, dt2));
// 18



// 48. Write a JavaScript function to get time differences in months between two dates. 
// Test Data :
// dt1 = new Date("June 13, 2014 08:11:00");
// dt2 = new Date("October 19, 2014 11:13:00");
// console.log(diff_months(dt1, dt2));
// 5



// 49. Write a JavaScript function to get time differences in years between two dates. 
// Test Data :
// dt1 = new Date("June 13, 2014 08:11:00");
// dt2 = new Date("October 19, 2017 11:13:00");
// console.log(diff_years(dt1, dt2));
// 3



// 50. Write a JavaScript function to get the week start date. 


// 51. Write a JavaScript function to get the week end date. 


// 52. Write a JavaScript function to get the month start date. 


// 53. Write a JavaScript function to get the month end date. 




Drawing.html // 1. Write a JavaScript program to draw the following rectangular shape.
// Expected Output :
// rectagular shape


// 2. Write a JavaScript program to draw a circle.
// Expected Output :
// draw a circle


// 3. Write a JavaScript program to draw two intersecting rectangles, one of which has alpha transparency.
// Expected Output :
// intersecting rectangles


// 4. Write a JavaScript program to draw the following right-angled triangle.
// Expected Output :
// right angled triangle


// 5. Write a JavaScript program to draw the following diagram [use moveto() function].
// Expected Output :
// draw fun


// 6. Write a JavaScript program to draw the following diagram [diagonal, white to black circles].
// Expected Output :
// diagonal, white to black circles




Functions.html // 1. Write a JavaScript function that reverse a number. 
// Example x = 32243;
// Expected Output : 34223


// 2. Write a JavaScript function that checks whether a passed string is palindrome or not? 
// A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.


// 3. Write a JavaScript function that generates all combinations of a string. 
// Example string : 'dog'
// Expected Output : d,do,dog,o,og,g


// 4. Write a JavaScript function that returns a passed string with letters in alphabetical order. 
// Example string : 'webmaster'
// Expected Output : 'abeemrstw'
// Assume punctuation and numbers symbols are not included in the passed string.


// 5. Write a JavaScript function that accepts a string as a parameter and converts the first letter of each word of the string in upper case. 
// Example string : 'the quick brown fox'
// Expected Output : 'The Quick Brown Fox '


// 6. Write a JavaScript function that accepts a string as a parameter and find the longest word within the string. 
// Example string : 'Web Development Tutorial'
// Expected Output : 'Development'


// 7. Write a JavaScript function that accepts a string as a parameter and counts the number of vowels within the string. 
// Note : As the letter 'y' can be regarded as both a vowel and a consonant, we do not count 'y' as vowel here.
// Example string : 'The quick brown fox'
// Expected Output : 5


// 8. Write a JavaScript function that accepts a number as a parameter and check the number is prime or not. 
// Note : A prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.


// 9. Write a JavaScript function which accepts an argument and returns the type. 
// Note : There are six possible values that typeof returns: object, boolean, function, number, string, and undefined.


// 10. Write a JavaScript function which returns the n rows by n columns identity matrix. 


// 11. Write a JavaScript function which will take an array of numbers stored and find the second lowest and second greatest numbers, respectively. 
// Sample array : [1,2,3,4,5]
// Expected Output : 2,4
// .

// 12. Write a JavaScript function which says whether a number is perfect. 
// According to Wikipedia : In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors, that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum). Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself).
// Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.
// .

// 13. Write a JavaScript function to compute the factors of a positive integer. 
// .

// 14. Write a JavaScript function to convert an amount to coins. 
// Sample function : amountTocoins(46, [25, 10, 5, 2, 1])
// Here 46 is the amount. and 25, 10, 5, 2, 1 are coins.
// Output : 25, 10, 10, 1
// .

// 15. Write a JavaScript function to compute the value of bn where n is the exponent and b is the bases. Accept b and n from the user and display the result. 
// .

// 16. Write a JavaScript function to extract unique characters from a string. 
// Example string : "thequickbrownfoxjumpsoverthelazydog"
// Expected Output : "thequickbrownfxjmpsvlazydg"
// .

// 17. Write a JavaScript function to  get the number of occurrences of each letter in specified string. 
// .

// 18. Write a function for searching JavaScript arrays with a binary search. 
// Note : A binary search searches by splitting an array into smaller and smaller chunks until it finds the desired value.
// .

// 19. Write a JavaScript function that returns array elements larger than a number. 
// .

// 20. Write a JavaScript function that generates a string id (specified length) of random characters. 
// Sample character list : "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
// .

// 21. Write a JavaScript function to get all possible subset with a fixed length (for example 2) combinations in an array. 
// Sample array : [1, 2, 3] and subset length is 2
// Expected output : [[2, 1], [3, 1], [3, 2], [3, 2, 1]]
// .

// 22. Write a JavaScript function that accepts two arguments, a string and a letter and the function will count the number of occurrences of the specified letter within the string. 
// Sample arguments : 'w3resource.com', 'o'
// Expected output : 2


// 23. Write a JavaScript function to find the first not repeated character. 
// Sample arguments : 'abacddbec'
// Expected output : 'e'


// 24. Write a JavaScript function to apply Bubble Sort algorithm. 
// Note : According to wikipedia "Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that works by repeatedly stepping through the list to be sorted, comparing each pair of adjacent items and swapping them if they are in the wrong order".
// Sample array : [12, 345, 4, 546, 122, 84, 98, 64, 9, 1, 3223, 455, 23, 234, 213]
// Expected output : [3223, 546, 455, 345, 234, 213, 122, 98, 84, 64, 23, 12, 9, 4, 1]


// 25. Write a JavaScript function that accept a list of country names as input and returns the longest country name as output. 
// Sample function : Longest_Country_Name(["Australia", "Germany", "United States of America"])
// Expected output : "United States of America"


// 26. Write a JavaScript function to find longest substring in a given a string without repeating characters. 


// 27. Write a JavaScript function that returns the longest palindrome in a given string. 

// Note: According to Wikipedia "In computer science, the longest palindromic substring or longest symmetric factor problem is the problem of finding a maximum-length contiguous substring of a given string that is also a palindrome. For example, the longest palindromic substring of "bananas" is "anana". The longest palindromic substring is not guaranteed to be unique; for example, in the string "abracadabra", there is no palindromic substring with length greater than three, but there are two palindromic substrings with length three, namely, "aca" and "ada".
// In some applications it may be necessary to return all maximal palindromic substrings (that is, all substrings that are themselves palindromes and cannot be extended to larger palindromic substrings) rather than returning only one substring or returning the maximum length of a palindromic substring.


// 28. Write a JavaScript program to pass a 'JavaScript function' as parameter. 


// 29. Write a JavaScript function to get the function name. 




Fundamentals (ES6).html 1. Write a JavaScript program to compare two objects to determine if the first one contains equivalent property values to the second one. 



2. Write a JavaScript program to copy a string to the clipboard. 



3. Write a JavaScript program to converts a comma-separated values (CSV) string to a 2D array. 



4. Write a JavaScript program to convert a comma-separated values (CSV) string to a 2D array of objects. The first row of the string is used as the title row. 



5. Write a JavaScript program to convert an array of objects to a comma-separated values (CSV) string that contains only the columns specified. 



6. Write a JavaScript program to target a given value in a nested JSON object, based on the given key. 



7. Write a JavaScript program to converts a specified number to an array of digits. 



8. Write a JavaScript program to filter out the specified values from a specified array. Return the original array without the filtered values. 



9. Write a JavaScript program to combine the numbers of a given array into an array containing all combinations. 



10. Write a JavaScript program to extract out the values at the specified indexes from a specified array. 



11. Write a JavaScript program to generate a random hexadecimal color code. 



12. Write a JavaScript program to removes non-printable ASCII characters from a given string. 



13. Write a JavaScript program to convert the length of a given string in bytes. 



14. Write a JavaScript program to replace the names of multiple object keys with the values provided. 



15. Write a JavaScript program to return the minimum-maximum value of an array, after applying the provided function to set comparing rule. 



16. Write a JavaScript function that returns true if the provided predicate function returns true for all elements in a collection, false otherwise. 



17. Write a JavaScript program to split values of two given arrays into two groups. If an element in filter is truthy, the corresponding element in the collection belongs to the first group; otherwise, it belongs to the second group. 



18. Write a JavaScript program to remove specified elements from the left of a given array of elements. 



19. Write a JavaScript program to remove specified elements from the right of a given array of elements. 



20. Write a JavaScript program to extend a 3-digit color code to a 6-digit color code. 



21. Write a JavaScript program to get every nth element in a given array. 



22. Write a JavaScript program to filter out the non-unique values in an array. 



23. Write a JavaScript program to filter out the non-unique values in an array, based on a provided comparator function. 



24. Write a JavaScript program to dcapitalize the first letter of a string. 



25. Write a JavaScript program to create a new array out of the two supplied by creating each possible pair from the arrays. 



26. Write a JavaScript program that will return true if the string is y/yes or false if the string is n/no. 



27. Write a JavaScript program to find every element that exists in any of the two given arrays once, using a provided comparator function. 



28. Write a JavaScript program to measure the time taken by a function to execute. 



29. Write a JavaScript program to convert a value to a safe integer. 



30. Write a JavaScript program to filter out the element(s) of a given array, that have one of the specified values. 



31. Write a JavaScript program to find all elements in a given array except for the first one. Return the whole array if the array's length is 1. 



32. Write a JavaScript program to get the sum of a given array, after mapping each element to a value using the provided function. 



33. Write a JavaScript program to get a random number in the specified range. 



34. Write a JavaScript program to get a random integer in the specified range. 



35. Write a JavaScript program to get an array of given n random integers in the specified range. 



36. Write a JavaScript program to create a function that invokes each provided function with the arguments it receives and returns the results. 



37. Write a JavaScript program to get a sorted array of objects ordered by properties and orders. 



38. Write a JavaScript program to pad a string on both sides with the specified character, if it's shorter than the specified length. 



39. Write a JavaScript program to remove the key-value pairs corresponding to the given keys from an object. 



40. Write a JavaScript program to create an array of key-value pair arrays from a given object. 



41. Write a JavaScript program to create an object from the given key-value pairs. 



42. Write a JavaScript program to get a customized coalesce function that returns the first argument that returns true from the provided argument validation function. 



43. Write a JavaScript program to change function that accepts an array into a variadic function. 



44. Write a JavaScript program to remove falsey values from a given array. 



45. Write a JavaScript program to split values into two groups, if an element in filter is truthy, the corresponding element in the collection belongs to the first group; otherwise, it belongs to the second group. 



46. Write a JavaScript program to curry (curries) a function. 



47. Write a JavaScript program to perform a deep comparison between two values to determine if they are equivalent. 



48. Write a JavaScript program to get an array of function property names from own (and optionally inherited) enumerable properties of an object. 



49. Write a JavaScript program to retrieve a set of properties indicated by the given selectors from an object. 



50. Write a JavaScript program to convert an integer to a suffixed string, adding am or pm based on its value. 



51. Write a JavaScript program to get an object containing the parameters of the current URL. 



52. Write a JavaScript program to group the elements of a given array based on the given function. 



53. Write a JavaScript program to Initialize a two dimension array of given width and height and value. 



54. Write a JavaScript program to initialize an array containing the numbers in the specified range where start and end are inclusive with their common difference step.



55. Write a JavaScript program to Join all given URL segments together, then normalizes the resulting URL. 



56. Write a JavaScript program to check whether all elements in a given array are equal or not. 



57. Write a JavaScript program to compute the average of an array, after mapping each element to a value using the provided function. 



58. Write a JavaScript program to split values into two groups according to a predicate function, which specifies which group an element in the input collection belongs to. 



59. Write a JavaScript program to create a function that invokes fn with a given context, optionally adding any additional supplied parameters to the beginning of the arguments. 



60. Write a JavaScript program to create a function that invokes the method at a given key of an object, optionally adding any additional supplied parameters to the beginning of the arguments. 



61. Write a JavaScript program to cast the provided value as an array if it's not one. 



62. Write a JavaScript program to chain asynchronous functions. 



63. Write a JavaScript program to clone a given regular expression. 



64. Write a JavaScript program to get the first non-null / undefined argument. 



65. Write a JavaScript program to add special characters to text to print in color in the console (combined with console.log()). 



66. Write a JavaScript program to perform right-to-left function composition. 



67. Write a JavaScript program to perform left-to-right function composition. 



68. Write a JavaScript program that accepts a converging function and a list of branching functions and returns a function that applies each branching function to the arguments and the results of the branching functions are passed as arguments to the converging function. 



69. Write a JavaScript program to group the elements of an array based on the given function and returns the count of elements in each group. 



70. Write a JavaScript program to count the occurrences of a value in an array. 



71. Write a JavaScript program to create a deep clone of an object. 



72. Write a JavaScript program to detect whether the website is being opened in a mobile device or a desktop/laptop. 



73. Write a JavaScript program to return the difference between two arrays, after applying the provided function to each array element of both. 



74. Write a JavaScript program to filter out all values from an array for which the comparator function does not return true. 



75. Write a JavaScript program to compute the new ratings between two or more opponents using the Elo rating system. It takes an array of pre-ratings and returns an array containing post-ratings. The array should be ordered from best performer to worst performer (winner -> loser). 



76. Write a JavaScript program to execute a provided function once for each array element, starting from the array's last element.



77. Write a JavaScript program to iterate over all own properties of an object, running a callback for each one. 



78. Write a JavaScript program to invert the key-value pairs of an object, without mutating it. The corresponding inverted value of each inverted key is an array of keys responsible for generating the inverted value. If a function is supplied, it is applied to each inverted key. 



79. Write a JavaScript program to take any number of iterable objects or objects with a length property and returns the longest one. 



80. Write a JavaScript program to implement the Luhn Algorithm used to validate a variety of identification numbers, such as credit card numbers, IMEI numbers, National Provider Identifier numbers etc. 



81. Write a JavaScript program to create an object with keys generated by running the provided function for each key and the same values as the provided object. 



82. Write a JavaScript program to map the values of an array to an object using a function, where the key-value pairs consist of the original value as the key and the mapped value. 



83. Write a JavaScript program to create a new string with the results of calling a provided function on every character in the calling string. 



84. Write a JavaScript program to create an object with the same keys as the provided object and values generated by running the provided function for each value. 



85. Write a JavaScript program to replace all but the last number of characters with the specified mask character. 



86. Write a JavaScript program to get the maximum value of an array, after mapping each element to a value using the provided function. 



87. Write a JavaScript program to get the n maximum elements from the provided array. If n is greater than or equal to the provided array's length, then return the original array(sorted in descending order). 



88. Write a JavaScript program to get the median of an array of numbers. 



89. Write a JavaScript program to negates a predicate function.



90. Write a JavaScript program to nest a given flat array of objects linked to one another recursively. 



91. Write a JavaScript program that will return true if the provided predicate function returns false for all elements in a collection, false otherwise. 



92. Write a JavaScript program to create a function that gets the argument at index n. If n is negative, the nth argument from the end is returned. 



93. Write a JavaScript program to remove an event listener from an element. 



94. Write a JavaScript program to move the specified amount of elements to the end of the array. 



95. Write a JavaScript program to add an event listener to an element with the ability to use event delegation. 



96. Write a JavaScript program to pick the key-value pairs corresponding to the given keys from an object. 



97. Write a JavaScript program to create an object composed of the properties the given function returns truthy for. The function is invoked with two arguments: (value, key). 



98. Write a JavaScript program to filter an array of objects based on a condition while also filtering out unspecified keys. 



99. Write a JavaScript program to hash a given input string into a whole number. 



100. Write a JavaScript program to create an array of elements, grouped based on the position in the original arrays and using function as the last value to specify how grouped values should be combined. 



101. Write a JavaScript program to return the object associating the properties to the values of a given array of valid property identifiers and an array of values. 



102. Write a JavaScript program to create an array of elements, grouped based on the position in the original arrays. 



103. Write a JavaScript program to convert a given string into an array of words. 



104. Write a JavaScript program to test a value, x, against a predicate function. If true, return fn(x). Else, return x. 



105. Write a JavaScript program that return true if the given value is a number, false otherwise. 



106. Write a JavaScript program to create an array of elements, ungrouping the elements in an array produced by zip and applying the provided function. 



107. Write a JavaScript program to get all unique values (form the right side of the array) of an array, based on a provided comparator function.



108. Write a JavaScript program to get all unique values of an array, based on a provided comparator function. 



109. Write a JavaScript program to get the nth element of a given array. 



110. Write a JavaScript program to get every element that exists in any of the two arrays once. 



111. Write a JavaScript program to build an array, using an iterator function and an initial seed value. 



112. Write a JavaScript program to unflatten an object with the paths for keys. 



113. Write a JavaScript program to unescape escaped HTML characters. 



114. Write a JavaScript program to uncurry a function up to depth n. 



115. Write a JavaScript program to create a function that accepts up to one argument, ignoring any additional arguments.



116. Write a JavaScript program to check if the predicate (second argument) is truthy on all elements of a collection (first argument). 



117. Write a JavaScript program to truncate a string up to a specified length. 



118. Write a JavaScript program to apply a function against an accumulator and each key in the object (from left to right). 



119. Write a JavaScript program to create tomorrow's date in a string representation. 



120. Write a JavaScript program to convert a string to snake case. 



121. Write a JavaScript program to convert a value to a safe integer. 



122. Write a JavaScript program to add an ordinal suffix to a number. 



123. Write a JavaScript program to convert a string to kebab case. 



124. Write a JavaScript program to reduce a given Array-like into a value hash (keyed data store). 



125. Write a JavaScript program to convert a float-point arithmetic to the Decimal mark form and It will make a comma separated string from a number. 



126. Write a JavaScript program to create a specified currency formatting from a given number. 



127. Write a JavaScript program to Iterate over a callback n times. 



128. Write a JavaScript program to get removed elements of a given array until the passed function returns true. 



129. Write a JavaScript program to get removed elements from the end of a given array until the passed function returns true. 



130. Write a JavaScript program to remove n elements from the end of a given array. 



131. Write a JavaScript program to get an array with n elements removed from the beginning from a given array 



132. Write a JavaScript program to get the symmetric difference between two given arrays, using a provided function as a comparator. 



133. Write a JavaScript program to get the symmetric difference between two given arrays, after applying the provided function to each array element of both. 



134. Write a JavaScript program to get the symmetric difference between two given arrays. 



135. Write a JavaScript program to get the sum of the powers of all the numbers from start to end (both inclusive). 



136. Write a JavaScript program to generate all permutations of a string (contains duplicates).



137. Write a JavaScript program to perform stable sorting of an array, preserving the initial indexes of items when their values are the same. Do not mutate the original array, but returns a new array instead. 



138. Write a JavaScript program that takes a variadic function and returns a closure that accepts an array of arguments to map to the inputs of the function. 



139. Write a JavaScript program to split a multiline string into an array of lines. 



140. Write a JavaScript program to get the highest index at which value should be inserted into array in order to maintain its sort order, based on a provided iterator function. 



141. Write a JavaScript program to get the highest index at which value should be inserted into array in order to maintain its sort order. 



142. Write a JavaScript program to get the lowest index at which value should be inserted into array in order to maintain its sort order.



143. Write a JavaScript program to sort the characters of a string Alphabetically. 



144. Write a JavaScript program to get an array of elements that appear in both arrays. 



145. Write a JavaScript program to randomize the order of the values of an array, returning a new array.



146. Write a JavaScript program to create a shallow clone of an object. 



147. Write a JavaScript program to serialize a cookie name-value pair into a Set-Cookie header string. 



148. Write a JavaScript program to hash the input string into a whole number. 



149. Write a JavaScript program to get a random element from an array. 



150. Write a JavaScript program to run a given array of promises in series. 





HTML DOM.html // 1. Here is a sample html file with a submit button. Now modify the style of the paragraph text through javascript code.
// Sample HTML file :

// <!DOCTYPE html>
// <html>
// <head>
// <meta charset=utf-8 />
// <title>JS DOM paragraph style</title>
// </head> 
// <body>
// <p id ='text'>JavaScript Exercises - w3resource</p> 
// <div>
// <button id="jsstyle"
// onclick="js_style()">Style</button>
// </div>
// </body>
// </html>

// Clicking on the button the font, font size, and color of the paragraph text will be changed.


// 2. Write a JavaScript function to get the values of First and Last name of the following form.
// Sample HTML file :

// <!DOCTYPE html>
// <html><head>
// <meta charset=utf-8 />
// <title>Return first and last name from a form - w3resource</title>
// </head><body>
// <form id="form1" onsubmit="getFormvalue()">
// First name: <input type="text" name="fname" value="David"><br>
// Last name: <input type="text" name="lname" value="Beckham"><br>
// <input type="submit" value="Submit">
// </form>
// </body>
// </html>



// 3. Write a JavaScript program to set the background color of a paragraph.


// 4. Here is a sample html file with a submit button. Write a JavaScript function to get the value of the href, hreflang, rel, target, and type attributes of the specified link.

// <!DOCTYPE html>
// <html><head>
// <meta charset=utf-8 />
// </head>
// <body>
// <p><a id="w3r" type="text/html" hreflang="en-us" rel="nofollow" target="_self" href="https://www.w3resource.com/">w3resource</a></p>
// <button onclick="getAttributes()">Click here to get  attributes value</button>
// </body></html>



// 5. Write a JavaScript function to add rows to a table.
// Sample HTML file :

// <!DOCTYPE html>
// <html><head>
// <meta charset=utf-8 />
// <title>Insert row in a table - w3resource</title>
// </head><body>
// <table id="sampleTable" border="1">
// <tr><td>Row1 cell1</td>
// <td>Row1 cell2</td></tr>
// <tr><td>Row2 cell1</td>
// <td>Row2 cell2</td></tr>
// </table><br>
// <input type="button" onclick="insert_Row()" value="Insert row"> 
// </body></html>



// 6. Write a JavaScript function that accept row, column, (to identify a particular cell) and a string to update the content of that cell.
// Sample HTML file :

// <!DOCTYPE html>
// <html><head>
// <meta charset=utf-8 />
// <title>Change the content of a cell</title>
// </head><body>
// <table id="myTable" border="1">
// <tr><td>Row1 cell1</td>
// <td>Row1 cell2</td></tr>
// <tr><td>Row2 cell1</td>
// <td>Row2 cell2</td></tr>
// <tr><td>Row3 cell1</td>
// <td>Row3 cell2</td></tr>
// </table><form>
// <input type="button" onclick="changeContent()" value="Change content">
// </form></body></html>



// 7. Write a JavaScript function that creates a table, accept row, column numbers from the user, and input row-column number as content (e.g. Row-0 Column-0) of a cell.
// Sample HTML file :

// <!DOCTYPE html>
// <html>
// <head>
// <meta charset=utf-8 />
// <title>Change the content of a cell</title>
// <style type="text/css">
// body {margin: 30px;}
// </style>  
// </head><body>
// <table id="myTable" border="1">
// </table><form>
// <input type="button" onclick="createTable()" value="Create the table">
// </form></body></html>



// 8. Write a JavaScript program to remove items from a dropdown list.
// Sample HTML file :

// <!DOCTYPE html>
// <html><head>
// <meta charset=utf-8 />
// <title>Remove items from a dropdown list</title>
// </head><body><form>
// <select id="colorSelect">
// <option>Red</option>
// <option>Green</option>
// <option>White</option>
// <option>Black</option>
// </select>
// <input type="button" onclick="removecolor()" value="Select and Remove">
// </form></body></html>



// 9. Write a JavaScript program to count and display the items of a dropdown list, in an alert window.
// Sample HTML file :

// <!DOCTYPE html>
// <html><head>
// <meta charset=utf-8 />
// <style type="text/css">
// body {margin: 30px;}
// </style>   
// <title>Count and display items of a dropdown list - w3resource</title>
// </head><body><form>
// Select your favorite Color :
// <select id="mySelect">
// <option>Red</option>
// <option>Green</option>
// <option>Blue</option>
// <option>White</option>
// </select>
// <input type="button" onclick="getOptions()" value="Count and Output all items">
// </form></body></html>



// 10. Write a JavaScript program to calculate the volume of a sphere.
// Sample Output of the form :

// volume sphere html form



// 11. Write a JavaScript program to display a random image (clicking on a button) from the following list.
// Sample Image information :

// "http://farm4.staticflickr.com/3691/11268502654_f28f05966c_m.jpg", width: "240", height: "160"
// "http://farm1.staticflickr.com/33/45336904_1aef569b30_n.jpg", width: "320", height: "195"
// "http://farm6.staticflickr.com/5211/5384592886_80a512e2c9.jpg", width: "500", height: "343"



// 12. Write a JavaScript program to highlight the bold words of the following paragraph, on mouse over a certain link.
// Sample link and text :
// [On mouse over here bold words of the following paragraph will be highlighted]
// We have just started this section for the users (beginner to intermediate) who want to work with various JavaScript problems and write scripts online to test their JavaScript skill.


// 13. Write a JavaScript program to get the width and height of the window (any time the window is resized).
//  



Math.html // 1. Write a JavaScript function to convert a number from one base to another. 
// Note : Both bases must be between 2 and 36.
// Test Data :
// console.log(base_convert('E164',16,8));
// console.log(base_convert(1000,2,8));
// "160544"
// "10"


// 2. Write a JavaScript function to convert a binary number to a decimal number. 
// Test Data :
// console.log(bin_to_dec('110011'));
// console.log(bin_to_dec('100'));
// 51
// 4


// 3. Write a JavaScript function to convert a decimal number to binary, hexadecimal or octal number. 
// Test Data :
// console.log(dec_to_bho(120,'B'));
// console.log(dec_to_bho(120,'H'));
// console.log(dec_to_bho(120,'O'));
// "1111000"
// "78"
// "170"


// 4. Write a JavaScript function to generate a random integer. 
// Test Data :
// console.log(rand(20,1));
// console.log(rand(1,10));
// console.log(rand(6));
// console.log(rand());
// 15
// 5
// 1
// 0


// 5. Write a JavaScript function to format a number up to specified decimal places. 
// Test Data :
// console.log(decimals(2.100212, 2));
// console.log(decimals(2.100212, 3));
// console.log(decimals(2100, 2));
// "2.10"
// "2.100"
// "2100.00"


// 6. Write a JavaScript function to find the highest value in an array. 
// Test Data :
// console.log(max([12,34,56,1]));
// console.log(max([-12,-34,0,-56,-1]));
// 56
// 0


// 7. Write a JavaScript function to find the lowest value in an array. 
// Test Data :
// console.log(min([12,34,56,1]));
// console.log(min([-12,-34,0,-56,-1]));
// 1
// -56


// 8. Write a JavaScript function to get the greatest common divisor (gcd) of two integers. 
// Note :
// According to Wikipedia - In mathematics, the greatest common divisor (gcd) of two or more integers, when at least one of them is not zero, is the largest positive integer that divides the numbers without a remainder. For example, the GCD of 8 and 12 is 4.

// Test Data :
// console.log(gcd_two_numbers(12, 13));
// console.log(gcd_two_numbers(9, 3));
// Output :
// 1
// 3


// 9. Write a JavaScript function to find the GCD (greatest common divisor) of more than 2 integers. 
// Test Data :
// console.log(gcd_more_than_two_numbers([3,15,27]));
// console.log(gcd_more_than_two_numbers([5,10,15,25]));
// Output :
// 3
// 5


// 10. Write a JavaScript function to get the least common multiple (LCM) of two numbers. 
// Note :
// According to Wikipedia - A common multiple is a number that is a multiple of two or more integers. The common multiples of 3 and 4 are 0, 12, 24, .... The least common multiple (LCM) of two numbers is the smallest number (not zero) that is a multiple of both.
// Test Data :
// console.log(lcm_two_numbers(3,15));
// console.log(lcm_two_numbers(10,15));
// Output :
// 15
// 30


// 11. Write a JavaScript function to get the least common multiple (LCM) of more than 2 integers. 
// Test Data :
// console.log(lcm_more_than_two_numbers([100,90,80,7]));
// console.log(lcm_more_than_two_numbers([5,10,15,25]));
// Output :
// 25200
// 150


// 12. Write a JavaScript function to find out if a number is a natural number or not. 
// Note :
// Natural numbers are whole numbers from 1 upwards : 1, 2, 3, and so on ... or from 0 upwards in some area of mathematics: 0, 1, 2, 3 and so on ...
// No negative numbers and no fractions.
// Test Data :
// console.log(is_Natural(-15));
// console.log(is_Natural(1));
// console.log(is_Natural(10.22));
// console.log(is_Natural(10/0));
// Output :
// false
// true
// false
// false


// 13. Write a JavaScript function to test if a number is a power of 2. 
// Test Data :
// console.log(power_of_2(16));
// console.log(power_of_2(18));
// console.log(power_of_2(256));
// Output :
// true
// false
// true


// 14. Write a JavaScript function to round a number to a given decimal places. 
// Test Data :
// console.log(precise_round(12.375,2));
// console.log(precise_round(12.37499,2));
// console.log(precise_round(-10.3079499, 3));
// Output :
// "12.38"
// "12.37"
// "-10.308"


// 15. Write a JavaScript function to check whether a value is an integer or not. 
// Note : Integer - A number which is not a fraction; a whole number.
// Test Data :
// console.log(is_Int(23));
// console.log(is_Int(4e2));
// console.log(is_Int(NaN));
// console.log(is_Int(23.75));
// console.log(is_Int(-23));
// Output :
// true
// true
// false
// false
// true


// 16. Write a JavaScript function to check to check whether a variable is numeric or not. 
// Test Data :
// console.log(is_Numeric(12));
// console.log(is_Numeric('abcd'));
// console.log(is_Numeric('12'));
// console.log(is_Numeric(' '));
// console.log(is_Numeric(1.20));
// console.log(is_Numeric(-200));
// Output :
// true
// false
// true
// false
// true
// true


// 17. Write a JavaScript function to calculate the sum of values in an array. 
// Test Data :
// console.log(sum([1,2,3]));
// console.log(sum([100,-200,3]));
// console.log(sum([1,2,'a',3]));
// Output :
// 6
// -97
// 6


// 18. Write a JavaScript function to calculate the product of values in an array. 
// Test Data :
// console.log(product([1,2,3]));
// console.log(product([100,-200,3]));
// console.log(product([1,2,'a',3]));
// Output :
// 6
// -60000
// 6


// 19. Create a Pythagorean function in JavaScript. 
// Note : The Pythagorean Theorem tells us that the relationship in every right triangle is : c2 = a2 + b2, where c is the hypotenuse and a, b are two legs of the triangle.
// Test Data :
// console.log(pythagorean_theorem(2, 4));
// console.log(pythagorean_theorem(3, 4));
// Output :
// 4.47213595499958
// 5


// 20. Write a JavaScript program to evaluate binomial coefficients. 
// Note :
// Binomial coefficient : According to Wikipedia - In mathematics, binomial coefficients are a family of positive integers that occur as coefficients in the binomial theorem. They are indexed by two nonnegative integers; the binomial coefficient indexed by n and k. Under suitable circumstances the value of the coefficient is given by the expression :
// binomial coefficients
// Arranging binomial coefficients into rows for successive values of n, and in which k ranges from 0 to n, gives a triangular array called Pascal's triangle.

// Test Data :
// console.log(binomial(8,3));
// console.log(binomial(10,2));
// Output :
// 56
// 45



// 21. Write a JavaScript function that Convert an integer into a Roman Numeral in javaScript. 



// 22. Write a JavaScript function that Convert Roman Numeral to Integer. 


// 23. Write a JavaScript function to create a UUID identifier. 
// Note :
// According to Wikipedia - A universally unique identifier (UUID) is an identifier standard used in software construction. A UUID is simply a 128-bit value. The meaning of each bit is defined by any of several variants. For human-readable display, many systems use a canonical format using hexadecimal text with inserted hyphen characters. For example : de305d54-75b4-431b-adb2-eb6b9e546014



// 24. Write a JavaScript function to round a number to a specified number of digits and strip extra zeros (if any). 
// Test Data :
// var a = -4.55555;
// console.log(result);
// -4.5556
// var a = 5.0001000;
// console.log(result);
// 5.0001


// 25. Write a JavaScript function to make currency math (add, subtract, multiply, division etc.). 
// Test Data :
// n1 = '$40.24', n2 = '$21.57';


// 26. Write a JavaScript function to calculate the nth root of a number. 
// Test Data :
// console.log(nthroot(64, 2));
// 8
// console.log(nthroot(64, -2));
// 0.125


// 27. Write a JavaScript function to calculate degrees between 2 points with inverse Y axis. 
// Test Data :
// console.log(pointDirection(1, 0, 12, 0));
// 0
// console.log(pointDirection(1, 0, 1, 10));
// 90


// 28. Write a JavaScript function to round up an integer value to the next multiple of 5. 
// Test Data :
// console.log(int_round5(32));
// 35
// console.log(int_round5(137));
// 140


// 29. Write a JavaScript function to convert a positive number to negative number. 
// Test Data :
// console.log(pos_to_neg(15));
// -15


// 30. Write a JavaScript function to cast a square root of a number to an integer. 
// Test Data :
// console.log(sqrt_to_int(17));
// 4


// 31. Write a JavaScript function to get the highest number from three different numbers. 
// Test Data :
// console.log(highest_of_three(-5, 4, 2));
// 4


// 32. Write a JavaScript function to calculate the percentage (%) of a number. 
// Test Data :
// console.log(percentage(1000, 47.12));
// 471.2


// 33. Write a JavaScript function to convert degrees to radians. 
// Test Data :
// console.log(degrees_to_radians(45));
// 0.7853981633974483


// 34. Write a JavaScript function to convert radians to degrees. 
// Test Data :
// console.log(radians_to_degrees(0.7853981633974483));
// 45


// 35. Write a JavaScript function for the Pythagorean theorem. 
// According to Wikipedia : In mathematics, the Pythagorean theorem, also known as Pythagoras' theorem, is a relation in Euclidean geometry among the three sides of a right triangle. It states that the square of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the other two sides. The theorem can be written as an equation relating the lengths of the sides a, b and c, often called the "Pythagorean equation".
// Test Data :
// console.log(pythagorean(4, 3));
// 5


// 36. Write a JavaScript function which will return values that are powers of two. 
// Test Data :
// console.log(isPower_of_two(64));
// true
// console.log(isPower_of_two(94));
// false


// 37. Write a JavaScript function to limit a value inside a certain range. 
// Note : If the value is higher than max it will return max. and if the value is smaller than min it will return the min.
// Test Data :
// console.log(value_limit(7, 1, 12));
// 7
// console.log(value_limit(-7, 0, 12));
// 0
// console.log(value_limit(15, 0, 12));
// 12


// 38. Write a JavaScript function to check if a number is a whole number or has a decimal place. 
// Note : Whole Numbers are simply the numbers 0, 1, 2, 3, 4, 5, ... (and so on). No Fractions!
// Test Data :
// console.log(number_test(25.66));
// "Number has a decimal place."
// console.log(number_test(10));
// "It is a whole number."


// 39. Write a JavaScript function to print an integer with commas as thousands separators. 
// Test Data :
// console.log(thousands_separators(1000));
// "1,000"
// console.log(thousands_separators(10000.23));
// "10,000.23"
// console.log(thousands_separators(100000));
// "100,000"


// 40. Write a JavaScript function to create random background color. 


// 41. Write a JavaScript function to count the digits of an integer. 


// 42. Write a JavaScript function to calculate the combination of n and r. 
// The formula is : n!/(r!*(n - r)!).
// Test Data :
// console.log(combinations(6, 2));
// 15
// console.log(combinations(5, 3));
// 10


// 43. Write a JavaScript function to get all prime numbers from 0 to a specified number. 
// Test Data :
// console.log(primeFactorsTo(5));
// [2, 3, 5]
// console.log(primeFactorsTo(15));
// [2, 3, 5, 7, 11, 13]


// 44. Write a JavaScript function to show the first twenty Hamming numbers. 
// Hamming Numbers are numbers whose only prime factors are 2, 3 and 5.


// 45. Write a JavaScript function to subtract elements from one another in an array. 


// 46. Write a JavaScript function to calculate the divisor and modulus of two integers. 


// 47. Write a JavaScript function to calculate the extended Euclid Algorithm or extended GCD. 
// In mathematics, the Euclidean algorithm[a], or Euclid's algorithm, is an efficient method for computing the greatest common divisor (GCD) of two numbers, the largest number that divides both of them without leaving a remainder. It is named after the ancient Greek mathematician Euclid, who first described it in Euclid's Elements. It is an example of an algorithm, a step-by-step procedure for performing a calculation according to well-defined rules, and is one of the oldest algorithms in common use. It can be used to reduce fractions to their simplest form, and is a part of many other number-theoretic and cryptographic calculations.


// 48. Write a JavaScript function to calculate the falling factorial of a number. 
// Let x be a real number (but usually an integer).
// Let k be a positive integer.
// Then x to the (power of) k falling is :
// kth falling factorial power of x
// This is called the kth falling factorial power of x.


// 49. Write a JavaScript function to calculate Lanczos approximation gamma. 
// In mathematics, the Lanczos approximation is a method for computing the Gamma function numerically, published by Cornelius Lanczos in 1964. It is a practical alternative to the more popular Stirling's approximation for calculating the Gamma function with fixed precision.


// 50. Write a JavaScript program to add two complex numbers. 
// A complex number is a number that can be expressed in the form a + bi, where a and b are real numbers and i is the imaginary unit, that satisfies the equation i2 = −1. In this expression, a is the real part and b is the imaginary part of the complex number.


// 51. Write a JavaScript program to subtract two complex numbers. 


// 52. Write a JavaScript program to multiply two complex numbers. 


// 53. Write a JavaScript program to divide two complex numbers. 




Object.html // 1. Write a JavaScript program to list the properties of a JavaScript object.
// Sample object:
// var student = {
// name : "David Rayy",
// sclass : "VI",
// rollno : 12 };
// Sample Output: name,sclass,rollno


// 2. Write a JavaScript program to delete the rollno property from the following object. Also print the object before or after deleting the property.
// Sample object:
// var student = {
// name : "David Rayy",
// sclass : "VI",
// rollno : 12 };


// 3. Write a JavaScript program to get the length of a JavaScript object.
// Sample object :
// var student = {
// name : "David Rayy",
// sclass : "VI",
// rollno : 12 };


// 4. Write a JavaScript program to display the reading status (i.e. display book name, author name and reading status) of the following books.

// var library = [ 
//    {
//        author: 'Bill Gates',
//        title: 'The Road Ahead',
//        readingStatus: true
//    },
//    {
//        author: 'Steve Jobs',
//        title: 'Walter Isaacson',
//        readingStatus: true
//    },
//    {
//        author: 'Suzanne Collins',
//        title:  'Mockingjay: The Final Book of The Hunger Games', 
//        readingStatus: false
//    }];



// 5. Write a JavaScript program to get the volume of a Cylinder with four decimal places using object classes.
// Volume of a cylinder : V = πr2h
// where r is the radius and h is the height of the cylinder.


// 6. Write a Bubble Sort algorithm in JavaScript.
// Note : Bubble sort is a simple sorting algorithm that works by repeatedly stepping through the list to be sorted,
// Sample Data: [6,4,0, 3,-2,1]
// Expected Output : [-2, 0, 1, 3, 4, 6]


// 7. Write a JavaScript program which returns a subset of a string.
// Sample Data: dog
// Expected Output: ["d", "do", "dog", "o", "og", "g"]


// 8. Write a JavaScript program to create a Clock.
// Note: The output will come every second.
// Expected Console Output :
// "14:37:42"
// "14:37:43"
// "14:37:44"
// "14:37:45"
// "14:37:46"
// "14:37:47"


// 9. Write a JavaScript program to calculate the area and perimeter of a circle.
// Note : Create two methods to calculate the area and perimeter. The radius of the circle will be supplied by the user.


// 10. Write a JavaScript program to sort an array of JavaScript objects.
// Sample Object :

// var library = [ 
//    {
//        title:  'The Road Ahead',
//        author: 'Bill Gates',
//        libraryID: 1254
//    },
//    {
//        title: 'Walter Isaacson',
//        author: 'Steve Jobs',
//        libraryID: 4264
//    },
//    {
//        title: 'Mockingjay: The Final Book of The Hunger Games',
//        author: 'Suzanne Collins',
//        libraryID: 3245
//    }];

// Expected Output:

// [[object Object] {
//   author: "Walter Isaacson",
//   libraryID: 4264,
//   title: "Steve Jobs"
// }, [object Object] {
//   author: "Suzanne Collins",
//   libraryID: 3245,
//   title: "Mockingjay: The Final Book of The Hunger Games"
// }, [object Object] {
//   author: "The Road Ahead",
//   libraryID: 1254,
//   title: "Bill Gates"
// }]



// 11. Write a JavaScript function to print all the methods in an JavaScript object.
// Test Data :
// console.log(all_properties(Array));
// ["length", "name", "arguments", "caller", "prototype", "isArray", "observe", "unobserve"]


// 12. Write a JavaScript function to parse an URL.


// 13. Write a JavaScript function to retrieve all the names of object's own and inherited properties.


// 14. Write a JavaScript function to retrieve all the values of an object's properties.


// 15. Write a JavaScript function to convert an object into a list of `[key, value]` pairs.


// 16. Write a JavaScript function to get a copy of the object where the keys have become the values and the values the keys.


// 17. Write a JavaScript function to check whether an object contains given property.


// 18. Write a JavaScript function to check whether a given value is a DOM element.




Recursion.html // 1. Write a JavaScript program to calculate the factorial of a number. 
// In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example, 5! = 5 x 4 x 3 x 2 x 1 = 120
// Click me to see the solution

// 2. Write a JavaScript program to find the greatest common divisor (gcd) of two positive numbers. 


// 3. Write a JavaScript program to get the integers in range (x, y). 
// Example : range(2, 9)
// Expected Output : [3, 4, 5, 6, 7, 8]


// 4. Write a JavaScript program to compute the sum of an array of integers. 
// Example : var array = [1, 2, 3, 4, 5, 6]
// Expected Output : 21


// 5. Write a JavaScript program to compute the exponent of a number. 
// Note : The exponent of a number says how many times the base number is used as a factor.
// 82 = 8 x 8 = 64. Here 8 is the base and 2 is the exponent.


// 6. Write a JavaScript program to get the first n Fibonacci numbers. 
// Note : The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, . . . Each subsequent number is the sum of the previous two.


// 7. Write a JavaScript program to check whether a number is even or not. 


// 8. Write a JavaScript program for binary search. 
// Sample array : [0,1,2,3,4,5,6]
// console.log(l.br_search(5)) will return '5'


// 9. Write a merge sort program in JavaScript. 
// Sample array : [34,7,23,32,5,62]
// Sample output : [5, 7, 23, 32, 34, 62]




String.html // 1. Write a JavaScript function to check whether an `input` is a string or not. 
// Test Data :
// console.log(is_string('w3resource'));
// true
// console.log(is_string([1, 2, 4, 0]));
// false
// Click me to see the solution

// 2. Write a JavaScript function to check whether a string is blank or not. 
// Test Data :
// console.log(is_Blank(''));
// console.log(is_Blank('abc'));
// true
// false
// Click me to see the solution

// 3. Write a JavaScript function to split a string and convert it into an array of words. 
// Test Data :
// console.log(string_to_array("Robin Singh"));
// ["Robin", "Singh"]
// Click me to see the solution

// 4. Write a JavaScript function to extract a specified number of characters from a string. 
// Test Data :
// console.log(truncate_string("Robin Singh",4));
// "Robi"


// 5. Write a JavaScript function to convert a string in abbreviated form. 
// Test Data :
// console.log(abbrev_name("Robin Singh"));
// "Robin S."


// 6. Write a JavaScript function to hide email addresses to protect from unauthorized user. 
// Test Data :
// console.log(protect_email("robin_singh@example.com"));
// "robin...@example.com"


// 7. Write a JavaScript function to parameterize a string. 
// Test Data :
// console.log(string_parameterize("Robin Singh from USA."));
// "robin-singh-from-usa"


// 8. Write a JavaScript function to capitalize the first letter of a string. 
// Test Data :
// console.log(capitalize('js string exercises'));
// "Js string exercises"


// 9. Write a JavaScript function to capitalize the first letter of each word in a string. 
// Test Data :
// console.log(capitalize_Words('js string exercises'));
// "Js String Exercises"


// 10. Write a JavaScript function that takes a string which has lower and upper case letters as a parameter and converts upper case letters to lower case, and lower case letters to upper case. 
// Test Data :
// console.log(swapcase('AaBbc'));
// "aAbBC"


// 11. Write a JavaScript function to convert a string into camel case.
// Test Data :
// console.log(camelize("JavaScript Exercises"));
// console.log(camelize("JavaScript exercises"));
// console.log(camelize("JavaScriptExercises"));
// "JavaScriptExercises"
// "JavaScriptExercises"
// "JavaScriptExercises"


// 12. Write a JavaScript function to uncamelize a string. 
// Test Data :
// console.log(uncamelize('helloWorld'));
// console.log(uncamelize('helloWorld','-'));
// console.log(uncamelize('helloWorld','_'));
// "hello world"
// "hello-world"
// "hello_world"


// 13. Write a JavaScript function to concatenates a given string n times (default is 1). 
// Test Data :
// console.log(repeat('Ha!'));
// console.log(repeat('Ha!',2));
// console.log(repeat('Ha!',3));
// "Ha!"
// "Ha!Ha!"
// "Ha!Ha!Ha!"


// 14. Write a JavaScript function to insert a string within a string at a particular position (default is 1).
// Test Data :
// console.log(insert('We are doing some exercises.'));
// console.log(insert('We are doing some exercises.','JavaScript '));
// console.log(insert('We are doing some exercises.','JavaScript ',18));
// "We are doing some exercises."
// "JavaScript We are doing some exercises."
// "We are doing some JavaScript exercises."


// 15. Write a JavaScript function to humanized number (Formats a number to a human-readable string.) with the correct suffix such as 1st, 2nd, 3rd or 4th. 
// Test Data :
// console.log(humanize_format());
// console.log(humanize_format(1));
// console.log(humanize_format(8));
// console.log(humanize_format(301));
// console.log(humanize_format(402));
// "1st"
// "8th"
// "301st"
// "402nd"


// 16. Write a JavaScript function to truncates a string if it is longer than the specified number of characters. Truncated strings will end with a translatable ellipsis sequence ("…") (by default) or specified characters. 
// Test Data :
// console.log(text_truncate('We are doing JS string exercises.'))
// console.log(text_truncate('We are doing JS string exercises.',19))
// console.log(text_truncate('We are doing JS string exercises.',15,'!!'))
// "We are doing JS string exercises."
// "We are doing JS ..."
// "We are doing !!"


// 17. Write a JavaScript function to chop a string into chunks of a given length. 
// Test Data :
// console.log(string_chop('w3resource'));
// console.log(string_chop('w3resource',2));
// console.log(string_chop('w3resource',3));
// ["w3resource"]
// ["w3", "re", "so", "ur", "ce"]
// ["w3r", "eso", "urc", "e"]


// 18. Write a JavaScript function to count the occurrence of a substring in a string. 
// Test Data :
// console.log(count("The quick brown fox jumps over the lazy dog", 'the'));
// Output :
// 2
// console.log(count("The quick brown fox jumps over the lazy dog", 'fox',false));
// Output :
// 1


// 19. Write a JavaScript function to escape a HTML string. 
// Test Data :
// console.log(escape_HTML('<a href="javascript-string-exercise-17.php" target="_blank">'));
// Output :
// "&lt;a href=&quot;javascript-string-exercise-17.php&quot; target=&quot;_blank&quot;&gt;"


// 20. Write a JavaScript function that can pad (left, right) a string to get to a determined length. 
// Test Data :
// console.log(formatted_string('0000',123,'l'));
// console.log(formatted_string('00000000',123,''));
// Output :
// "0123"
// "12300000"


// 21. Write a JavaScript function to repeat a string a specified times. 
// Test Data :
// console.log(repeat_string('a', 4));
// console.log(repeat_string('a'));
// Output :
// "aaaa"
// "Error in string or count."


// 22. Write a JavaScript function to get a part of a string after a specified character.
// Test Data :
// console.log(subStrAfterChars('w3resource: JavaScript Exercises', ':','a'));
// console.log(subStrAfterChars('w3resource: JavaScript Exercises', 'E','b'));
// Output :
// "w3resource"
// "xercises"


// 23. Write a JavaScript function to strip leading and trailing spaces from a string. 
// Test Data :
// console.log(strip('w3resource '));
// console.log(strip(' w3resource'));
// console.log(strip(' w3resource '));
// Output :
// "w3resource"
// "w3resource"
// "w3resource"


// 24. Write a JavaScript function to truncate a string to a certain number of words. 
// Test Data :
// console.log(truncate('The quick brown fox jumps over the lazy dog', 4));
// Output :
// "The quick brown fox"


// 25. Write a JavaScript function to alphabetize a given string. 
// Alphabetize string : An individual string can be alphabetized. This rearranges the letters so they are sorted A to Z.
// Test Data :
// console.log(alphabetize_string('United States'));
// Output :
// "SUadeeinsttt"


// 26. Write a JavaScript function to remove the first occurrence of a given 'search string' from a string. 
// Test Data :
// console.log(remove_first_occurrence("The quick brown fox jumps over the lazy dog", 'the'));
// Output :
// "The quick brown fox jumps over lazy dog"


// 27. Write a JavaScript function to convert ASCII to Hexadecimal format. 
// Test Data :
// console.log(ascii_to_hexa('12'));
// console.log(ascii_to_hexa('100'));
// Output :
// "3132"
// "313030"


// 28. Write a JavaScript function to convert Hexadecimal to ASCII format. 
// Test Data :
// console.log(hex_to_ascii('3132'));
// console.log(hex_to_ascii('313030'));
// Output :
// "12"
// "100"


// 29. Write a JavaScript function to find a word within a string. 
// Test Data :
// console.log(search_word('The quick brown fox', 'fox'));
// console.log(search_word('aa, bb, cc, dd, aa', 'aa'));
// Output :
// "'fox' was found 1 times."
// "'aa' was found 2 times."


// 30. Write a JavaScript function check if a string ends with specified suffix. 
// Test Data :
// console.log(string_endsWith('JS PHP PYTHON','PYTHON'));
// true
// console.log(string_endsWith('JS PHP PYTHON',''));
// false


// 31. Write a JavaScript function to escapes special characters (&, <, >, ', ") for use in HTML. 
// Test Data :
// console.log(escape_html('PHP & MySQL'));
// "PHP &amp; MySQL"
// console.log(escape_html('3 > 2'));
// "3 &gt; 2"


// 32. Write a JavaScript function to remove?non-printable ASCII chars. 
// Test Data :
// console.log(remove_non_ascii('???????PHP-MySQL??????'));
// "PHP-MySQL"


// 33. Write a JavaScript function to remove non-word characters. 
// Test Data :
// console.log(remove_non_word('PHP ~!@#$%^&*()+`-={}[]|\\:";\'/?><., MySQL'));
// "PHP - MySQL"


// 34. Write a JavaScript function to convert a string to title case. 
// Test Data :
// console.log(sentenceCase('PHP exercises. python exercises.'));
// "Php Exercises. Python Exercises."


// 35. Write a JavaScript function to remove HTML/XML tags from string. 
// Test Data :
// console.log(strip_html_tags('<p><strong><em>PHP Exercises</em></strong></p>'));
// "PHP Exercises"


// 36. Write a JavaScript function to create a Zerofilled value with optional +, - sign. 
// Test Data :
// console.log(zeroFill(120, 5, '-'));
// "+00120"
// console.log(zeroFill(29, 4));
// "0029"


// 37. Write a JavaScript function to test case insensitive (except special Unicode characters) string comparison. 
// Test Data :
// console.log(compare_strings('abcd', 'AbcD'));
// true
// console.log(compare_strings('ABCD', 'Abce'));
// false


// 38. Write a JavaScript function to create a case-insensitive search. 
// Test Data :
// console.log(case_insensitive_search('JavaScript Exercises', 'exercises'));
// "Matched"
// console.log(case_insensitive_search('JavaScript Exercises', 'Exercises'));
// "Matched"
// console.log(case_insensitive_search('JavaScript Exercises', 'Exercisess'));
// "Not Matched"


// 39. Write a JavaScript function to Uncapitalize? the first character of a string. 
// Test Data :
// console.log(Uncapitalize('Js string exercises'));
// "js string exercises"


// 40. Write a JavaScript function to Uncapitalize the first letter of each word of a string. 
// Test Data :
// console.log(unCapitalize_Words('Js String Exercises'));
// "js string exercises"


// 41. Write a JavaScript function to capitalize each word in the string. 
// Test Data :
// console.log(capitalizeWords('js string exercises'));
// "JS STRING EXERCISES"


// 42. Write a JavaScript function to uncapitalize each word in the string. 
// Test Data :
// console.log(unCapitalizeWords('JS STRING EXERCISES'));
// "js string exercises"


// 43. Write a JavaScript function to test whether the character at the provided (character) index is upper case. 
// Test Data :
// console.log(isUpperCaseAt('Js STRING EXERCISES', 1));
// false


// 44. Write a JavaScript function to test whether the character at the provided (character) index is lower case. 
// Test Data :
// console.log(isLowerCaseAt ('Js STRING EXERCISES', 1));
// true


// 45. Write a JavaScript function to get humanized number with the correct suffix such as 1st, 2nd, 3rd or 4th. 
// Test Data :
// console.log(humanize(1));
// console.log(humanize(20));
// console.log(humanize(302));
// "1st"
// "20th"
// "302nd"


// 46. Write a JavaScript function to test whether a string starts with a specified string. 
// Test Data :
// console.log(startsWith('js string exercises', 'js'));
// true


// 47. Write a JavaScript function to test whether a string ends with a specified string. 
// Test Data :
// console.log(endsWith('JS string exercises', 'exercises'));
// true


// 48. Write a JavaScript function to get the successor of a string. 

// Note: The successor is calculated by incrementing characters starting from the rightmost alphanumeric (or the rightmost character if there are no alphanumerics) in the string. Incrementing a digit always results in another digit, and incrementing a letter results in another letter of the same case. If the increment generates a carry, the character to the left of it is incremented. This process repeats until there is no carry, adding an additional character if necessary.
// Example :
// string.successor("abcd") == "abce"
// string.successor("THX1138") == "THX1139"
// string.successor("< >") == "< >"
// string.successor("1999zzz") == "2000aaa"
// string.successor("ZZZ9999") == "AAAA0000"

// Test Data :
// console.log(successor('abcd'));
// console.log(successor('3456'));
// "abce"
// "3457"


// 49. Write a JavaScript function to get unique guid (an acronym for 'Globally Unique Identifier?) of the specified length, or 32 by default. 
// Test Data :
// console.log(guid());
// console.log(guid(15));
// "hRYilcoV7ajokxsYFl1dba41AyE0rUQR"
// "b7pwBqrZwqaDrex"




Validation and Regular Expression.html // 1. Write a JavaScript program to test the first character of a string is uppercase or not.


// 2. Write a JavaScript program to check a credit card number.


// 3. Write a pattern that matches e-mail addresses.
// The personal information part contains the following ASCII characters.

//     Uppercase (A-Z) and lowercase (a-z) English letters.
//     Digits (0-9).
//     Characters ! # $ % & ' * + - / = ? ^ _ ` { | } ~
//     Character . ( period, dot or fullstop) provided that it is not the first or last character and it will not come one after the other.



// 4. Write a JavaScript program to search a date within a string.



// 5. Write a JavaScript program that work as a trim function (string) using regular expression.



// 6. Write a JavaScript program to count number of words in string.
// Note :
// - Remove white-space from start and end position.
// - Convert 2 or more spaces to 1.
// - Exclude newline with a start spacing.



// 7. Write a JavaScript function to check whether a given value is IP value or not.



// 8. Write a JavaScript function to count the number of vowels in a given string.
// Test Data :
// console.log(alphabetize_string('United States'));
// Output :
// "SUadeeinsttt"



// 9. Write a JavaScript function to check whether a given value is an valid url or not.



// 10. Write a JavaScript function to check whether a given value is alpha numeric or not.



// 11. Write a JavaScript function to check whether a given value is time string or not.



// 12. Write a JavaScript function to check whether a given value is US zip code or not.



// 13. Write a JavaScript function to check whether a given value is UK Post Code or not.



// 14. Write a JavaScript function to check whether a given value is Canada Post Code or not.



// 15. Write a JavaScript function to check whether a given value is a social security number or not.



// 16. Write a JavaScript function to check whether a given value is hexadecimal value or not.



// 17. Write a JavaScript function to check whether a given value is hexcolor value or not.



// 18. Write a JavaScript function to check whether a given value represents a domain or not.



// 19. Write a JavaScript function to check whether a given value is html or not.Go to the editor



// 20. Write a JavaScript function to check a given value contains alpha, dash and underscore.



// 21. Write a JavaScript function to print an integer with commas as thousands separators.

// Test Data :
// console.log(thousands_separators(1000));
// "1,000"
// console.log(thousands_separators(10000.23));
// "10,000.23"
// console.log(thousands_separators(100000));
// "100,000"





Array.html // 1. Write a JavaScript function to check whether an `input` is an array or not. 
// Test Data :
// console.log(is_array('w3resource'));
// console.log(is_array([1, 2, 4, 0]));
// false
// true


// 2. Write a JavaScript function to clone an array. 
// Test Data :
// console.log(array_Clone([1, 2, 4, 0]));
// console.log(array_Clone([1, 2, [4, 0]]));
// [1, 2, 4, 0]
// [1, 2, [4, 0]]


// 3. Write a JavaScript function to get the first element of an array. Passing a parameter 'n' will return the first 'n' elements of the array. 
// Test Data :
// console.log(first([7, 9, 0, -2]));
// console.log(first([],3));
// console.log(first([7, 9, 0, -2],3));
// console.log(first([7, 9, 0, -2],6));
// console.log(first([7, 9, 0, -2],-3));
// Expected Output :
// 7
// []
// [7, 9, 0]
// [7, 9, 0, -2]
// []


// 4. Write a JavaScript function to get the last element of an array. Passing a parameter 'n' will return the last 'n' elements of the array. 
// Test Data :
// console.log(last([7, 9, 0, -2]));
// console.log(last([7, 9, 0, -2],3));
// console.log(last([7, 9, 0, -2],6));
// Expected Output :
// -2
// [9, 0, -2]
// [7, 9, 0, -2]


// 5. Write a simple JavaScript program to join all elements of the following array into a string. 
// Sample array : myColor = ["Red", "Green", "White", "Black"];
// Expected Output :
// "Red,Green,White,Black"
// "Red,Green,White,Black"
// "Red+Green+White+Black"


// 6. Write a JavaScript program which accept a number as input and insert dashes (-) between each two even numbers. For example if you accept 025468 the output should be 0-254-6-8. 


// 7. Write a JavaScript program to sort the items of an array. 
// Sample array : var arr1 = [ 3, 8, 7, 6, 5, -4, 3, 2, 1 ];
// Sample Output : -4,-3,1,2,3,5,6,7,8


// 8. Write a JavaScript program to find the most frequent item of an array. 
// Sample array : var arr1=[3, 'a', 'a', 'a', 2, 3, 'a', 3, 'a', 2, 4, 9, 3];
// Sample Output : a ( 5 times )


// 9. Write a JavaScript program which accept a string as input and swap the case of each character. For example if you input 'The Quick Brown Fox' the output should be 'tHE qUICK bROWN fOX'. 


// 10. Write a JavaScript program which prints the elements of the following array. 
// Note : Use nested for loops.
// Sample array : var a = [[1, 2, 1, 24], [8, 11, 9, 4], [7, 0, 7, 27], [7, 4, 28, 14], [3, 10, 26, 7]];
// Sample Output :
// "row 0"
// " 1"
// " 2"
// " 1"
// " 24"
// "row 1"
// ------
// ------


// 11. Write a JavaScript program to find the sum of squares of a numeric vector. 


// 12. Write a JavaScript program to compute the sum and product of an array of integers. 


// 13. Write a JavaScript program to add items in an blank array and display the items. 
// Sample Screen :
// add elements in an blank array


// 14. Write a JavaScript program to remove duplicate items from an array (ignore case sensitivity). 


// 15. We have the following arrays : 
// color = ["Blue ", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow "];
// o = ["th","st","nd","rd"]
// Write a JavaScript program to display the colors in the following way :
// "1st choice is Blue ."
// "2nd choice is Green."
// "3rd choice is Red."
// - - - - - - - - - - - - -
// Note : Use ordinal numbers to tell their position.


// 16. Find the leap years in a given range of years. 


// 17. Write a JavaScript program to shuffle an array. 


// 18. Write a JavaScript program to perform a binary search. 
// Note : A binary search or half-interval search algorithm finds the position of a specified input value within an array sorted by key value.
// Sample array :
// var items = [1, 2, 3, 4, 5, 7, 8, 9];
// Expected Output :
// console.log(binary_Search(items, 1)); //0
// console.log(binary_Search(items, 5)); //4


// 19. There are two arrays with individual values, write a JavaScript program to compute the sum of each individual index value from the given arrays. 
// Sample array :
// array1 = [1,0,2,3,4];
// array2 = [3,5,6,7,8,13];
// Expected Output :
// [4, 5, 8, 10, 12, 13]


// 20. Write a JavaScript program to find duplicate values in a JavaScript array. 


// 21. Write a JavaScript program to flatten a nested (any depth) array. If you pass shallow, the array will only be flattened a single level. 
// Sample Data :
// console.log(flatten([1, [2], [3, [[4]]],[5,6]]));
// [1, 2, 3, 4, 5, 6]
// console.log(flatten([1, [2], [3, [[4]]],[5,6]], true));
// [1, 2, 3, [[4]], 5, 6]


// 22. Write a JavaScript program to compute the union of two arrays. 
// Sample Data :
// console.log(union([1, 2, 3], [100, 2, 1, 10]));
// [1, 2, 3, 10, 100]


// 23. Write a JavaScript function to find the difference of two arrays. 
// Test Data :
// console.log(difference([1, 2, 3], [100, 2, 1, 10]));
// ["3", "10", "100"]
// console.log(difference([1, 2, 3, 4, 5], [1, [2], [3, [[4]]],[5,6]]));
// ["6"]
// console.log(difference([1, 2, 3], [100, 2, 1, 10]));
// ["3", "10", "100"]


// 24. Write a JavaScript function to remove. 'null', '0', '""', 'false', 'undefined' and 'NaN' values from an array. 
// Sample array : [NaN, 0, 15, false, -22, '',undefined, 47, null]
// Expected result : [15, -22, 47]


// 25. Write a JavaScript function to sort the following array of objects by title value. 
// Sample object :

// var library = [ 
//    { author: 'Bill Gates', title: 'The Road Ahead', libraryID: 1254},
//    { author: 'Steve Jobs', title: 'Walter Isaacson', libraryID: 4264},
//    { author: 'Suzanne Collins', title: 'Mockingjay: The Final Book of The Hunger Games', libraryID: 3245}
//    ];

// Expected result :

// [[object Object] {
//   author: "Suzanne Collins",
//   libraryID: 3245,
//   title:"Mockingjay:The Final Book of The Hunger Games"
// }, [object Object] {
//   author: "Bill Gates",
//   libraryID: 1254,
//   title: "The Road Ahead"
// }, [object Object] {
//   author: "Steve Jobs",
//   libraryID: 4264,
//   title: "Walter Isaacson"
// }]



// 26. Write a JavaScript program to find a pair of elements (indices of the two numbers) from an given array whose sum equals a specific target number. 

// Input: numbers= [10,20,10,40,50,60,70], target=50
// Output: 2, 3



// 27. Write a JavaScript function to retrieve the value of a given property from all elements in an array. 
// Sample array : [NaN, 0, 15, false, -22, '',undefined, 47, null]
// Expected result : [15, -22, 47]


// 28. Write a JavaScript function to find the longest common starting substring in a set of strings. 

// Sample array : console.log(longest_common_starting_substring(['go', 'google']));
// Expected result : "go"



// 29. Write a JavaScript function to fill an array with values (numeric, string with one character) on supplied bounds. 

// Test Data :
// console.log(num_string_range('a', "z", 2));
// ["a", "c", "e", "g", "i", "k", "m", "o", "q", "s", "u", "w", "y"]



// 30. Write a JavaScript function to merge two arrays and removes all duplicates elements. 

// Test data :
// var array1 = [1, 2, 3];
// var array2 = [2, 30, 1];
// console.log(merge_array(array1, array2));
// [3, 2, 30, 1]



// 31. Write a JavaScript function to remove a specific element from an array. 

// Test data :
// console.log(remove_array_element([2, 5, 9, 6], 5));
// [2, 9, 6]


// 32. Write a JavaScript function to find an array contains a specific element. 

// Test data :
// arr = [2, 5, 9, 6];
// console.log(contains(arr, 5));
// [True]


// 33. Write a JavaScript script to empty an array keeping the original. 



// 34. Write a JavaScript function to get nth largest element from an unsorted array. 

// Test Data :
// console.log(nthlargest([ 43, 56, 23, 89, 88, 90, 99, 652], 4));
// 89



// 35. Write a JavaScript function to get a random item from an array. 



// 36. Write a JavaScript function to create a specified number of elements with pre-filled numeric value array. 

// Test Data :
// console.log(array_filled(6, 0));
// [0, 0, 0, 0, 0, 0]
// console.log(array_filled(4, 11));
// [11, 11, 11, 11]



// 37. Write a JavaScript function to create a specified number of elements with pre-filled string value array. 

// Test Data :
// console.log(array_filled(3, 'default value'));
// ["default value", "default value", "default value"]
// console.log(array_filled(4, 'password'));
// ["password", "password", "password", "password"]


// 38. Write a JavaScript function to move an array element from one position to another. 

// Test Data :
// console.log(move([10, 20, 30, 40, 50], 0, 2));
// [20, 30, 10, 40, 50]
// console.log(move([10, 20, 30, 40, 50], -1, -2));
// [10, 20, 30, 50, 40]


// 39. Write a JavaScript function to filter false, null, 0 and blank values from an array. 

// Test Data :
// console.log(filter_array_values([58, '', 'abcd', true, null, false, 0]));
// [58, "abcd", true]


// 40. Write a JavaScript function to generate an array of specified length, filled with integer numbers, increase by one from starting position. 

// Test Data :
// console.log(array_range(1, 4));
// [1, 2, 3, 4]
// console.log(array_range(-6, 4));
// [-6, -5, -4, -3]


// 41. Write a JavaScript function to generate an array between two integers of 1 step length. 

// Test Data :
// console.log(rangeBetwee(4, 7));
// [4, 5, 6, 7]
// console.log(rangeBetwee(-4, 7));
// [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]


// 42. Write a JavaScript function to find the unique elements from two arrays. 

// Test Data :
// console.log(difference([1, 2, 3], [100, 2, 1, 10]));
// ["1", "2", "3", "10", "100"]
// console.log(difference([1, 2, 3, 4, 5], [1, [2], [3, [[4]]],[5,6]]));
// ["1", "2", "3", "4", "5", "6"]
// console.log(difference([1, 2, 3], [100, 2, 1, 10]));
// ["1", "2", "3", "10", "100"]






Basics.html  1. Write a JavaScript program to display the current day and time in the following format.  
 Sample Output : Today is : Tuesday.
 Current time is : 10 PM : 30 : 38

HTML
<!DOCTYPE html>
  <html>
  <head>
  <meta charset="utf-8">
  <title>JavaScript current day and time</title>
  </head>
  <body></body>
</html>

JS
var today = new Date();
  var day = today.getDay();
  var daylist = ["Sunday","Monday","Tuesday","Wednesday ","Thursday","Friday","Saturday"];
  console.log("Today is : " + daylist[day] + ".");
  var hour = today.getHours();
  var minute = today.getMinutes();
  var second = today.getSeconds();
  var prepand = (hour >= 12)? " PM ":" AM ";
  hour = (hour >= 12)? hour - 12: hour;
  if (hour===0 && prepand===' PM ') 
  { 
  if (minute===0 && second===0)
  { 
  hour=12;
  prepand=' Noon';
  } 
  else
  { 
  hour=12;
  prepand=' PM';
  } 
  } 
  if (hour===0 && prepand===' AM ') 
  { 
  if (minute===0 && second===0)
  { 
  hour=12;
  prepand=' Midnight';
  } 
  else
  { 
  hour=12;
  prepand=' AM';
  } 
  } 
console.log("Current Time : "+hour + prepand + " : " + minute + " : " + second);


 2. Write a JavaScript program to print the contents of the current window.  

HTML Code:
<!DOCTYPE HTML>
<html>
<head>
<meta charset=utf-8 />
<title>Print the current page.</title>
</head>
<body>
<p>Click the button to print the current page.</p>
<button onclick="print_current_page()">Print this page</button>
</body>
</html>

JavaScript Code:
function print_current_page()
{
window.print();
}

 3. Write a JavaScript program to get the current date.  
 Expected Output :
 mm-dd-yyyy, mm/dd/yyyy or dd-mm-yyyy, dd/mm/yyyy

HTML Code:
<!DOCTYPE html>
  <html>
  <head>
  <meta charset="utf-8">
  <title>Write a JavaScript program to get the current date.</title>
  </head>
  <body>
  </body>
  </html>

JavaScript Code:
var today = new Date();
var dd = today.getDate();

var mm = today.getMonth()+1; 
var yyyy = today.getFullYear();
if(dd<10) 
{
    dd='0'+dd;
} 

if(mm<10) 
{
    mm='0'+mm;
} 
today = mm+'-'+dd+'-'+yyyy;
console.log(today);
today = mm+'/'+dd+'/'+yyyy;
console.log(today);
today = dd+'-'+mm+'-'+yyyy;
console.log(today);
today = dd+'/'+mm+'/'+yyyy;
console.log(today);

 4. Write a JavaScript program to find the area of a triangle where lengths of the three of its sides are 5, 6, 7.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
<meta charset=utf-8 />
<title>The area of a triangle</title>
</head>
<body>  
</body>
</html>

JavaScript Code:

var side1 = 5; 
var side2 = 6; 
var side3 = 7; 
var s = (side1 + side2 + side3)/2;
var area =  Math.sqrt(s*((s-side1)*(s-side2)*(s-side3)));
console.log(area);

 5. Write a JavaScript program to rotate the string 'w3resource' in right direction by periodically removing one letter from the end of the string and attaching it to the front.  

HTML Code:

<!DOCTYPE html>
  <html> 
  <head>
  <title>JavaScript basic animation</title>
  <script type="text/javascript">
  </script>
  </head> <body onload="animate_string('target')"
  <pre id="target">w3resource </pre>
  </body> 
  </html>
  
JavaScript Code:

function animate_string(id) 
{
    var element = document.getElementById(id);
    var textNode = element.childNodes[0];  assuming no other children
    var text = textNode.data;

setInterval(function () 
{
 text = text[text.length - 1] + text.substring(0, text.length - 1);
  textNode.data = text;
}, 100);
}

 6. Write a JavaScript program to determine whether a given year is a leap year in the Gregorian calendar.  

HTML Code:

<!DOCTYPE html>
<html>
<head>
<meta charset=utf-8 />
<title>Find Leap Year</title>
</head>
<body>
</body>
</html>


JavaScript Code:

function leapyear(year)
{
return (year % 100 === 0) ? (year % 400 === 0) : (year % 4 === 0);
}
console.log(leapyear(2016));
console.log(leapyear(2000));
console.log(leapyear(1700));
console.log(leapyear(1800));
console.log(leapyear(100));

 7. Write a JavaScript program to find 1st January is being a Sunday between 2014 and 2050.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
<meta charset=utf-8 />
<title>A Program to find 1st January is being a Sunday between 2014 and 2050.</title>
</head>
<body>
</body>
</html>


JavaScript Code:

console.log('--------------------');
for (var year = 2014; year <= 2050; year++)
    {
    var d = new Date(year, 0, 1);
    if ( d.getDay() === 0 )
        console.log("1st January is being a Sunday  "+year);
    }
console.log('--------------------');


 8. Write a JavaScript program where the program takes a random integer between 1 to 10, the user is then prompted to input a guess number. If the user input matches with guess number, the program will display a message "Good Work" otherwise display a message "Not matched".  
HTML Code:

<!DOCTYPE html>
<html>
<head>
<meta charset=utf-8 />
<title>Guess a number</title>
</head>
<body>
</body>
</html>


JavaScript Code:

 Get a random integer from 1 to 10 inclusive
 const num = Math.ceil(Math.random() * 10);
console.log(num);
 const gnum = prompt('Guess the number between 1 and 10 inclusive');
 if (gnum == num)
   console.log('Matched');
  else
   console.log('Not matched, the number was '+gnum);
   

 9. Write a JavaScript program to calculate days left until next Christmas.  
HTML Code:

<!DOCTYPE html>
  <html>
  <head>
  <meta charset=utf-8 />
  <title>Write a JavaScript program to calculate days left until next Christmas</title>
  </head>
  <body>
</body>
  </html>
  


JavaScript Code:

today=new Date();
var cmas=new Date(today.getFullYear(), 11, 25);
if (today.getMonth()==11 && today.getDate()>25) 
{
cmas.setFullYear(cmas.getFullYear()+1); 
}  
var one_day=1000*60*60*24;
console.log(Math.ceil((cmas.getTime()-today.getTime())/(one_day))+
" days left until Christmas!");

 10. Write a JavaScript program to calculate multiplication and division of two numbers (input from user).  
 Sample form :
 sample form

HTML Code:

<!DOCTYPE html>
<html> 
<head>
<meta charset=utf-8 />
<title>JavaScript program to calculate multiplication and division of two numbers </title>
<style type="text/css">
body {margin: 30px;}
</style> 
</head>
<body>
<form>
1st Number : <input type="text" id="firstNumber" /><br>
2nd Number: <input type="text" id="secondNumber" /><br>
<input type="button" onClick="multiplyBy()" Value="Multiply" />
<input type="button" onClick="divideBy()" Value="Divide" />
</form>
<p>The Result is : <br>
<span id = "result"></span>
</p>
</body>
</html>


JavaScript Code:

function multiplyBy()
{
        num1 = document.getElementById("firstNumber").value;
        num2 = document.getElementById("secondNumber").value;
        document.getElementById("result").innerHTML = num1 * num2;
}

function divideBy() 
{ 
        num1 = document.getElementById("firstNumber").value;
        num2 = document.getElementById("secondNumber").value;
document.getElementById("result").innerHTML = num1 / num2;
}


11. Write a JavaScript program to convert temperatures to and from Celsius, Fahrenheit.  
[ Formula : c/5 = (f-32)/9 [ where c = temperature in Celsius and f = temperature in Fahrenheit ]
Expected Output :
60°C is 140 °F
45°F is 7.222222222222222°C

HTML Code:

<!DOCTYPE html>
  <html>
  <head>
  <meta charset="utf-8">
  <title>Write a JavaScript program to convert temperatures to and from celsius, fahrenheit</title>
  </head>
  <body>
</body>
  </html>
  


JavaScript Code:

function cToF(celsius) 
{
  var cTemp = celsius;
  var cToFahr = cTemp * 9 / 5 + 32;
  var message = cTemp+'\xB0C is ' + cToFahr + ' \xB0F.';
    console.log(message);
}

function fToC(fahrenheit) 
{
  var fTemp = fahrenheit;
  var fToCel = (fTemp - 32) * 5 / 9;
  var message = fTemp+'\xB0F is ' + fToCel + '\xB0C.';
    console.log(message);
} 
cToF(60);
fToC(45);


 12. Write a JavaScript program to get the website URL (loading page).  
HTML Code:

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Write a JavaScript program to get the website URL (loading page)</title>
</head>
<body>
</body>
</html>


JavaScript Code:

//Write a JavaScript program to get the website URL (loading page)
console.log(document.URL);

 13. Write a JavaScript exercise to create a variable using a user-defined name.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Create a variable using a user-defined name</title>
</head>
<body>

</body>
</html>


JavaScript Code:

var var_name = 'abcd';
var n = 120;
this[var_name] = n;
console.log(this[var_name])

 14. Write a JavaScript exercise to get the extension of a filename.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>The extension of a filename.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

filename = "system.php"
console.log(filename.split('.').pop());
filename = "abc.js"
console.log(filename.split('.').pop());

 15. Write a JavaScript program to get the difference between a given number and 13, if the number is greater than 13 return double the absolute difference.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>The difference between a given number and 13, if the number is greater than 13 return double the absolute difference.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function difference(n)
 {
    if (n <= 13)
        return 13 - n;
    else
        return (n - 13) * 2;
 }
console.log(difference(32))
console.log(difference(11))

 16. Write a JavaScript program to compute the sum of the two given integers. If the two values are same, then returns triple their sum.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to compute the sum of the two given integers. If the two values are same, then return triple their sum</title>
</head>
<body>
</body>
</html>


JavaScript Code:

function sumTriple (x, y) {
  if (x == y) {
    return 3 * (x + y);
    } 
   else
   {
    return (x + y);
   }
 }
console.log(sumTriple(10, 20));
console.log(sumTriple(10, 10));


 17. Write a JavaScript program to compute the absolute difference between a specified number and 19. Returns triple their absolute difference if the specified number is greater than 19.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to compute the absolute difference between a specified number and 19.  Returns triple their absolute difference if the specified number is greater than 19.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function diff_num(n) {
  if (n <= 19) {
    return (19 - n);
    }
  else
    {
     return (n - 19) * 3;
    }
}

console.log(diff_num(12));
console.log(diff_num(19));
console.log(diff_num(22));

 18. Write a JavaScript program to check two given numbers and return true if one of the number is 50 or if their sum is 50.  

HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check two given numbers and return true if one of the number is 50 or if their sum is 50.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function test50(x, y) 
{
  return ((x == 50 || y == 50) || (x + y == 50));
}
console.log(test50(50, 50))
console.log(test50(20, 50))
console.log(test50(20, 20))
console.log(test50(20, 30))

 19. Write a JavaScript program to check whether a given integer is within 20 of 100 or 400.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check whether a given integer is within 20 of 100 or 400.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function testhundred(x) {
  return ((Math.abs(100 - x) <= 20) ||
   (Math.abs(400 - x) <= 20));
}

console.log(testhundred(10));
console.log(testhundred(90));
console.log(testhundred(99));
console.log(testhundred(199));
console.log(testhundred(200));


 20. Write a JavaScript program to check from two given integers, whether one is positive and another one is negative.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to  check from two given integers, whether one is positive and another one is negative.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function positive_negative(x, y)
{
  if ((x < 0 && y > 0) || x > 0 && y < 0) 
  {
    return true;
  }
  else 
  {
    return false;
  }
}
console.log(positive_negative(2, 2));
console.log(positive_negative(-2, 2));
console.log(positive_negative(2, -2));
console.log(positive_negative(-2, -2));

 21. Write a JavaScript program to create a new string adding "Py" in front of a given string. If the given string begins with "Py" then return the original string.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to create a new string adding “Py” in front of a given string.  If the given string begins with “Py” then return the original string.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function string_check(str1) {
  if (str1 === null || str1 === undefined || str1.substring(0, 2) === 'Py') 
  {
    return str1;
  }
  return "Py"+str1;
}

console.log(string_check("Python"));
console.log(string_check("thon"));

 22. Write a JavaScript program to remove a character at the specified position of a given string and return the new string.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to remove a character at the specified position of a given string and return the new string.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function remove_character(str, char_pos) 
 {
  part1 = str.substring(0, char_pos);
  part2 = str.substring(char_pos + 1, str.length);
  return (part1 + part2);
 }

console.log(remove_character("Python",0));
console.log(remove_character("Python",3));
console.log(remove_character("Python",5));

 23. Write a JavaScript program to create a new string from a given string changing the position of first and last characters. The string length must be greater than or equal to 1.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to create a new string from a given string changing the position of first and last characters.</title>
</head>
<body>
</body>
</html>


JavaScript Code:

function first_last(str1) 
  {
  if (str1.length <= 1)
  {
    return str1;
  }
  mid_char = str1.substring(1, str1.length - 1);
  return (str1.charAt(str1.length - 1)) + mid_char + str1.charAt(0);
}
console.log(first_last('a'));
console.log(first_last('ab'));
console.log(first_last('abc'));

 24. Write a JavaScript program to create a new string from a given string with the first character of the given string added at the front and back.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to create a new string from a given string with the first character of the given string added at the front and back.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function front_back(str)
{
  first = str.substring(0,1);
  return first + str + first;
}
console.log(front_back('a'));
console.log(front_back('ab'));
console.log(front_back('abc'));

 25. Write a JavaScript program to check whether a given positive number is a multiple of 3 or a multiple of 7.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check whether a given positive number is a multiple of 3 or a multiple of 7. </title>
</head>
<body>

</body>
</html>


JavaScript Code:

function test37(x) 
{
  if (x % 3 == 0 || x % 7 == 0) 
  {
    return true;
  } 
  else {
    return false;
  }
}

console.log(test37(12));
console.log(test37(14));
console.log(test37(10));
console.log(test37(11));

 26. Write a JavaScript program to create a new string from a given string taking the last 3 characters and added at both the front and back. The string length must be 3 or more.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to create a new string from a given string taking the last 3 characters and added at both the front and back. The string length must be 3 or more.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function front_back3(str)
 {
  if (str.length>=3)
   {
   str_len = 3;
 
  back = str.substring(str.length-3);
   return back + str + back;
 }
   else
     return false;
 }
console.log(front_back3("abc"));
console.log(front_back3("ab"));
console.log(front_back3("abcd"));

 27. Write a JavaScript program to check whether a string starts with 'Java' and false otherwise.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check whether a string starts with 'Java' and false otherwise.</title>
</head>
<body>
</body>
</html>


JavaScript Code:

function start_spec_str(str)
{
  if (str.length < 4)
  {
    return false;
  }
  front = str.substring(0, 4);
  if (front == 'Java') 
  {
    return true;
  }
   else 
   {
    return false;
  }
}

console.log(start_spec_str("JavaScript"));
console.log(start_spec_str("Java"));
console.log(start_spec_str("Python"));

 28. Write a JavaScript program to check whether two given integer values are in the range 50..99 (inclusive). Return true if either of them are in the said range.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check whether two given integer values are in the range 50..99 (inclusive). Return true if either of them are in the said range.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function check_numbers(x, y) 
  {
  if ((x >= 50 && x <= 99) || (y >= 50 && y <= 99))
  {
    return true;
  } 
  else 
  {
    return false;
  }
}

console.log(check_numbers(12, 101));
console.log(check_numbers(52, 80));
console.log(check_numbers(15, 99));

 29. Write a JavaScript program to check whether three given integer values are in the range 50..99 (inclusive). Return true if one or more of them are in the said range.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check whether three given integer values are in the range 50..99 (inclusive). Return true if one or more of them are in the said range.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function check_three_nums(x, y, z) 
{
  return (x >= 50 && x <= 99) || (y >= 50 && y <= 99) || (z >= 50 && z <= 99);
}

console.log(check_three_nums(50, 90, 99));
console.log(check_three_nums(5, 9, 199));
console.log(check_three_nums(65, 89, 199));
console.log(check_three_nums(65, 9, 199));

 30. Write a JavaScript program to check whether a string "Script" presents at 5th (index 4) position in a given string, if "Script" presents in the string return the string without "Script" otherwise return the original one.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check whether a string “Script” presents at 5th (index 4) position in a given string, if “Script” presents in the string return the string without “Script” otherwise return the original one.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function check_script(str)
{
  if (str.length < 6) {
    return str;
  }
  let result_str = str;
    
  if (str.substring(10, 4) == 'Script') 
    {
    
   result_str = str.substring(0, 4) + str.substring(10,str.length);
      
  }
  return result_str;
}

console.log(check_script("JavaScript"));
console.log(check_script("CoffeeScript"));

 31. Write a JavaScript program to find the largest of three given integers.  

HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to find the largest of three given integers.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function max_of_three(x, y, z) 
 {
  max_val = 0;
  if (x > y)
  {
    max_val = x;
  } else
  {
    max_val = y;
  }
  if (z > max_val) 
  {
    max_val = z;
  }
  return max_val;
}

console.log(max_of_three(1,0,1));
console.log(max_of_three(0,-10,-20));
console.log(max_of_three(1000,510,440));


 32. Write a JavaScript program to find a value which is nearest to 100 from two different given integer values.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to find a value which is nearest to 100 from two different given integer values.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function near_100(x, y) {
  if (x != y)
  {
  x1 = Math.abs(x - 100);
  y1 = Math.abs(y - 100);

  if (x1 < y1)
  {
    return x;
  }
  if (y1 < x1)
  {
    return y;
  }
  return 0;
  }
  else
    return false;
}

console.log(near_100(90, 89));
console.log(near_100(-90, -89));
console.log(near_100(90, 90));

 33. Write a JavaScript program to check whether two numbers are in range 40..60 or in the range 70..100 inclusive.  

HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check whether two numbers are in range 40..60 or in the range 70..100 inclusive</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function numbers_ranges(x, y) {
  if ((x >= 40 && x <= 60 && y >= 40 && y <= 60) 
      || 
      (x >= 70 && x <= 100 && y >= 70 && y <= 100))
     {
    return true;
     } 
    else 
     {
    return false;
  }
}

console.log(numbers_ranges(44, 56));
console.log(numbers_ranges(70, 95));
console.log(numbers_ranges(50, 89));  


 34. Write a JavaScript program to find the larger number from the two given positive integers, the two numbers are in the range 40..60 inclusive.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to find the larger number from the two given positive integers, the two numbers  are in the range 40..60 inclusive.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function max_townums_range(x, y){ 
if( (x >= 40) && (x <= 60) && (y >= 40 && y <= 60) ){
if(x === y){
return "Numbers are the same";
}else if (x > y){
return x;
}else{
return y;
}
}else{
return "Numbers don't fit in range";
}
}

console.log(max_townums_range(45, 60));
console.log(max_townums_range(25, 60));
console.log(max_townums_range(45, 80));

 35. Write a program to check whether a specified character exists within the 2nd to 4th position in a given string.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check a given string contains 2 to 4 numbers of a specified character.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function check_char(str1, char)
 {
  ctr = 0;
  for (let i = 0; i < str1.length; i++)
  {
    if ((str1.charAt(i) == char) && (i >= 1 && i <= 3))
    {
        ctr=1;
        break;
    }
   }
   if (ctr==1) return true;
   return false;
}
console.log(check_char("Python", "y"));
console.log(check_char("JavaScript", "a"));
console.log(check_char("Console", "o"));
console.log(check_char("Console", "C"));
console.log(check_char("Console", "e"));
console.log(check_char("JavaScript", "S"));

 36. Write a JavaScript program to check whether the last digit of the three given positive integers is same.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check whether the last digit of the three given positive integers is same.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function last_digit(x, y, z)
{
  if ((x > 0) && y > 0 && z > 0)
    {
     return (x % 10 == y % 10 && y % 10 == z % 10 && x % 10 == z % 10);
   }
  else
    return false;
}

console.log(last_digit(20, 30, 400));
console.log(last_digit(-20, 30, 400));
console.log(last_digit(20, -30, 400));
console.log(last_digit(20, 30, -400));

 37. Write a JavaScript program to create new string with first 3 characters are in lower case from a given string. If the string length is less than 3 convert all the characters in upper case.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to create new string with first 3 characters are in lower case from a given string. If the string length is less than 3 convert all the characters in upper case.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function upper_lower(str) {
  if (str.length < 3) {
    return str.toUpperCase();
  }
  front_part = (str.substring(0, 3)).toLowerCase();
  back_part = str.substring(3, str.length);  
  return front_part + back_part;
}
console.log(upper_lower("Python"));
console.log(upper_lower("Py"));
console.log(upper_lower("JAVAScript"));

 38. Write a JavaScript program to check the total marks of a student in various examinations. The student will get A+ grade if the total marks are in the range 89..100 inclusive, if the examination is "Final-exam." the student will get A+ grade and total marks must be greater than or equal to 90. Return true if the student get A+ grade or false otherwise.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check the total marks of a student in various examinations</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function exam_status(totmarks,is_exam)
  {
  if (is_exam) {
    return totmarks >= 90;
  }
 return (totmarks >= 89 && totmarks <= 100);
 }

console.log(exam_status("78", " "));
console.log(exam_status("89", "true "));
console.log(exam_status("99", "true "));

39. Write a JavaScript program to compute the sum of the two given integers, If the sum is in the range 50..80 return 65 other wise return 80.  

HTML Code:
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to compute the sum of the two given integers, If the sum is in the range 50..80  return 65 other wise return 80.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function sortaSum(x, y) 
 {
  const sum_nums = x + y;
  if (sum_nums >= 50 && sum_nums <= 80) {
    return 65;
  }
  return 80;
}

console.log(sortaSum(30,20));
console.log(sortaSum(90,80));

 40. Write a JavaScript program to check from two given integers whether one of them is 8 or their sum or difference is 8.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Write a JavaScript program to check from two given integers whether one of them is 8 or their sum or difference is 8.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function check8(x, y) {
  if (x == 8 || y == 8) {
    return true;
  }

  if (x + y == 8 || Math.abs(x - y) == 8)
  {
    return true;
  }

  return false;
}

console.log(check8(7, 8));
console.log(check8(16, 8));
console.log(check8(24, 32));
console.log(check8(17, 18));

 41. Write a JavaScript program to check three given numbers, if the three numbers are same return 30 otherwise return 20 and if two numbers are same return 40.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check three given numbers, if the three numbers are same return 30 otherwise return 20 and if two numbers are same return 40.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function three_numbers(x, y, z) {
  if (x == y && y == z) {
    return 30;
  }

  if (x == y || y == z || z == x) {
    return 40;
  }

  return 20;
}
console.log(three_numbers(8, 8, 8));
console.log(three_numbers(8, 8, 18));
console.log(three_numbers(8, 7, 18));


 42. Write a JavaScript program to check whether three given numbers are increasing in strict mode or in soft mode.  
 Note: Strict mode -> 10, 15, 31 : Soft mode -> 24, 22, 31 or 22, 22, 31
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Write a JavaScript program to check whether three given numbers are increasing in strict mode or in soft mode.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function number_order(x, y, z ) {
  if ( y > x && z > y) 
  {
    return "strict mode";    
  }
  else if(z > y) 
   return "Soft mode";
  else
    return "Undefinded";
}

console.log(number_order(10,15,31));
console.log(number_order(24,22,31));
console.log(number_order(50,21,15));

 43. Write a JavaScript program to check from three given numbers (non negative integers) that two or all of them have the same rightmost digit.  

HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check from three  given numbers (non negative integers) that two  or all of them have the same rightmost digit.</title>
</head>
<body>
</body>
</html>


JavaScript Code:

function same_last_digit(p, q, r) {
    return (p % 10 === q % 10) ||
           (p % 10 === r % 10) ||
           (q % 10 === r % 10);
           
}

console.log(same_last_digit(22,32,42));
console.log(same_last_digit(102,302,2));
console.log(same_last_digit(20,22,45));

 44. Write a JavaScript program to check from three given integers that whether a number is greater than or equal to 20 and less than one of the others.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check from three given integers that whether a number is greater than or equal to 20 and less than one of the others.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function lessby20_others(x, y, z) 
{
return (x >= 20 && (x < y || x < z)) ||
(y >= 20 && (y < x || y < z)) ||
(z >= 20 && (z < y || z < x));
}
console.log(lessby20_others(23, 45, 10));
console.log(lessby20_others(23, 23, 10));
console.log(lessby20_others(21, 66, 75));

45. Write a JavaScript program to check two given integer values and return true if one of the number is 15 or if their sum or difference is 15.  

HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check two given integer values and return true if one of the number is 15 or if their sum or difference is 15.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function test_number(x, y) {
    return (x === 15 || y === 15 || x + y === 15 || Math.abs(x - y) === 15);
}

console.log(test_number(15, 9));
console.log(test_number(25, 15));
console.log(test_number(7, 8));
console.log(test_number(25, 10));
console.log(test_number(5, 9));
console.log(test_number(7, 9));
console.log(test_number(9, 25));

 46. Write a JavaScript program to check two given non-negative integers that whether one of the number (not both) is multiple of 7 or 11.  

HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check two given non-negative integers that whether one of the number (not both) is multiple of 7 or 11.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function valCheck (a, b) {
if (!((a % 7 == 0 || a % 11 == 0) && (b % 7 == 0 || b % 11 == 0))) {
return ((a % 7 == 0 || a % 11 == 0) || (b % 7 == 0 || b % 11 == 0));
}
else
return false;
}
console.log(valCheck(14, 21));
console.log(valCheck(14, 20));
console.log(valCheck(16, 20));

 47. Write a JavaScript program to check whether a given number is presents in the range 40..10000.  
 For example 40 presents in 40 and 4000

HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check whether a given number is presents in the range 40..10000. </title>
</head>
<body>

</body>
</html>


JavaScript Code:

function test_digit(x, y, n) 
  {    
    if (n < 40 || n > 10000)
      return false;
    else
      if (n >= x && n <= y)
        return true;
      else
        return false;
  }
console.log(test_digit(40, 4000, 45));  
console.log(test_digit(80, 320, 79));  
console.log(test_digit(89, 4000, 30));

 48. Write a JavaScript program to reverse a given string.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to reverse a given string.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function string_reverse(str) 
{
    return str.split("").reverse().join("");
}

console.log(string_reverse("w3resource"));
console.log(string_reverse("www"));
console.log(string_reverse("JavaScript"));

 49. Write a JavaScript program to replace every character in a given string with the character following it in the alphabet.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to replace every character in a given string with the character following it in the alphabet.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function string_reverse(str) 
function LetterChanges(text) {
//https://goo.gl/R8gn7u
var s = text.split('');
for (var i = 0; i < s.length; i++) {
// Caesar cipher
switch(s[i]) {
case ' ':
break;
case 'z':
s[i] = 'a';
break;
case 'Z': 
s[i] = 'A';
break;
default:
s[i] = String.fromCharCode(1 + s[i].charCodeAt(0));
}

// Upper-case vowels
switch(s[i]) {
case 'a': case 'e': case 'i': case 'o': case 'u':
s[i] = s[i].toUpperCase();
}
}
return s.join('');
}
console.log(LetterChanges("PYTHON"));
console.log(LetterChanges("W3R"));
console.log(LetterChanges("php"));

 50. Write a JavaScript program to capitalize the first letter of each word of a given string.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to capitalize the first letter of each word of a given string.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function capital_letter(str) 
{
    str = str.split(" ");

    for (var i = 0, x = str.length; i < x; i++) {
        str[i] = str[i][0].toUpperCase() + str[i].substr(1);
    }

    return str.join(" ");
}

console.log(capital_letter("Write a JavaScript program to capitalize the first letter of each word of a given string."))

 51. Write a JavaScript program to convert a given number to hours and minutes.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to convert a given number to hours and minutes.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function time_convert(num)
 { 
  var hours = Math.floor(num / 60);  
  var minutes = num % 60;
  return hours + ":" + minutes;         
}

console.log(time_convert(71));
console.log(time_convert(450));
console.log(time_convert(1441));

 52. Write a JavaScript program to convert the letters of a given string in alphabetical order.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to convert the letters of a given string  in alphabetical order.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function alphabet_Soup(str) { 

    return str.split("").sort().join("");
         
}

console.log(alphabet_Soup("Python"));

console.log(alphabet_Soup("Exercises"));


 53. Write a JavaScript program to check whether the characters a and b are separated by exactly 3 places anywhere (at least once) in a given string.  

HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to check whether the characters a and b are separated by exactly 3 places anywhere (at least once) in a given string.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function ab_Check(str)
 {
    return (/a...b/).test(str) || (/b...a/).test(str);
 }

console.log(ab_Check("Chainsbreak"));
console.log(ab_Check("pane borrowed"));
console.log(ab_Check("abCheck"));

 54. Write a JavaScript program to count the number of vowels in a given string.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to count the number of vowels in a given string.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function vowel_Count(str)
{ 

  return str.replace(/[^aeiou]/g, "").length; 
}

console.log(vowel_Count("Python"));
console.log(vowel_Count("w3resource.com"));

 55. Write a JavaScript program to check whether a given string contains equal number of p's and t's.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>check whether a given string contains equal number of p's and t's</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function equal_pt(str)
{ 
  var str_p = str.replace(/[^p]/g, "");

  var str_t = str.replace(/[^t]/g, "");

  var p_num = str_p.length;
  var s_num = str_t.length;

  return p_num === s_num;
         
}
console.log(equal_pt("paatpss"));
console.log(equal_pt("paatps"));

 56. Write a JavaScript program to divide two positive numbers and return a string with properly formatted commas.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to divide two positive numbers and return a string with properly formatted commas.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function division_string(n1, n2) {
  
n1 = 80;
n2 = 6;

var div = Math.round(n1 / n2).toString(),
result_array = div.split("");

if (div >= 1000)
{
for (var i = div.length - 3; i > 0; i -= 3) 
{
result_array.splice(i, 0, ",");
}
result_array;
}
console.log(result_array);

 57. Write a JavaScript program to create a new string of specified copies (positive number) of a given string.  

HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to create a new string of specified copies of a given string.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function string_copies (str, n) 
{
  if (n < 0)
    return false;
  else
  return str.repeat(n);
}
console.log(string_copies("abc", 5));
console.log(string_copies("abc", 0));
console.log(string_copies("abc", -2));

 58. Write a JavaScript program to create a new string of 4 copies of the last 3 characters of a given original string. The length of the given string must be 3 and above.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to create a new string of 4 copies of the last 3 characters of a given original string. The length of the given string must be 3 and above.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function newstring(str)
{
  if (str.length >= 3) {
    result_str = str.substring(str.length - 3);
    return result_str + result_str + result_str + result_str;
  }
  else
    return false;
}
console.log(newstring("Python 3.0"));
console.log(newstring("JS"));
console.log(newstring("JavaScript"));


 59. Write a JavaScript program to extract the first half of a string of even length.  
HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to  extract the first half of a string of even length.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function first_half (str) {
  if (str.length % 2 == 0) {
    return str.slice(0, str.length / 2);
  }
  return str;
}
console.log(first_half("Python"));  
console.log(first_half("JavaScript")); 
console.log(first_half("PHP"));

 60. Write a JavaScript program to create a new string without the first and last character of a given string.  

HTML Code:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JavaScript program to create a new string without the first and last character of a given string.</title>
</head>
<body>

</body>
</html>


JavaScript Code:

function without_first_end(str) {
  return str.substring(1, str.length - 1);
}
console.log(without_first_end('JavaScript'));
console.log(without_first_end('JS'));
console.log(without_first_end('PHP'));

 61. Write a JavaScript program to concatenate two strings except their first character.  


 62. Write a JavaScript program to move last three character to the start of a given string. The string length must be greater or equal to three.  


 63. Write a JavaScript program to create a string using the middle three characters of a given string of odd length. The string length must be greater or equal to three.  


 64. Write a JavaScript program to concatenate two strings and return the result. If the length of the strings are not same then remove the characters from the longer string.  


 65. Write a JavaScript program to test whether a string end with "Script". The string length must be greater or equal to 6.  


 66. Write a JavaScript program to display the city name if the string begins with "Los" or "New" otherwise return blank.  


 67. Write a JavaScript program to create a new string from a given string, removing the first and last characters of the string if the first or last character are 'P'. Return the original string if the condition is not satisfied.  


 68. Write a JavaScript program to create a new string using the first and last n characters from a given sting. The string length must be greater or equal to n.  


 69. Write a JavaScript program to compute the sum of three elements of a given array of integers of length 3.  


 70. Write a JavaScript program to rotate the elements left of a given array of integers of length 3.  


 71. Write a JavaScript program to check whether 1 appears in first or last position of a given array of integers. The array length must be greater or equal to 1.  


 72. Write a JavaScript program to check whether the first and last elements are equal of a given array of integers length 3.  


 73. Write a JavaScript program to reverse the elements of a given array of integers length 3.  


 74. Write a JavaScript program to find the larger value between the first or last and set all the other elements with that value. Display the new array.  


 75. Write a JavaScript program to create a new array taking the middle elements of the two arrays of integer and each length 3.  


 76. Write a JavaScript program to create a new array taking the first and last elements from a given array of integers and length must be greater or equal to 1.  


 77. Write a JavaScript program to test whether an array of integers of length 2 contains 1 or a 3.  


 78. Write a JavaScript program to test whether an array of integers of length 2 does not contain 1 or a 3.  


 79. Write a JavaScript program to test whether a given array of integers contains 30 and 40 twice. The array length should be 0, 1, or 2.  


 80. Write a JavaScript program to swap the first and last elements of a given array of integers. The array length should be at least 1.  


 81. Write a JavaScript program to add two digits of a given positive integer of length two.  


 82. Write a JavaScript to add two positive integers without carry.  


 83. Write a JavaScript to find the longest string from a given array of strings.  


 84. Write a JavaScript to replace each character of a given string by the next one in the English alphabet.  
 Note: 'a' will be replace by 'b' or 'z' would be replaced by 'a'.


 85. Write a JavaScript code to divide a given array of positive integers into two parts. First element goes to first part, second element goes to second part, and third element goes to first part and so on. Now compute the sum of two parts and store into an array of size two.  


 86. Write a JavaScript program to find the types of a given angle.  

     Types of angles:
     Acute angle: An angle between 0 and 90 degrees.
     Right angle: An 90 degree angle.
     Obtuse angle: An angle between 90 and 180 degrees.
     Straight angle: A 180 degree angle.



 87. Write a JavaScript program to check whether two arrays of integers of same length are similar or not. The arrays will be similar if one array can be obtained from another array by swapping at most one pair of elements.  


 88. Write a JavaScript program to check whether two given integers are similar or not, if a given divisor divides both integers and it does not divide either.  


 89. Write a JavaScript program to check whether it is possible to replace $ in a given expression x $ y = z with one of the four signs +, -, * or / to obtain a correct expression.  
 For example x = 10, y = 30 and z = 300, we can replace $ with a multiple operator (*) to obtain x * y = z


 90. Write a JavaScript program to find the kth greatest element of a given array of integers  


 91. Write a JavaScript program to find the maximum possible sum of some of its k consecutive numbers (numbers that follow each other in order.) of a given array of positive integers. 


 92. Write a JavaScript program to find the maximal difference between any two adjacent elements of a given array of integers. 


 93. Write a JavaScript program to find the maximal difference among all possible pairs of a given array of integers. 


 94. Write a JavaScript program to find the number which appears most in a given array of integers. 


 95. Write a JavaScript program to replace all the numbers with a specified number of a given array of integers. 


 96. Write a JavaScript program to compute the sum of absolute differences of consecutive numbers of a given array of integers. 


 97. Write a JavaScript program to find the shortest possible string which can create a string to make it a palindrome by adding characters to the end of it. 


 98. Write a JavaScript program to switch case of the minimum possible number of letters to make a given string written in the upper case or in the lower case. 
 Fox example "Write" will be write and "PHp" will be "PHP"


 99. Write a JavaScript program to check whether it is possible to rearrange characters of a given string in such way that it will become equal to another given string. 


 100. Write a JavaScript program to check whether there is at least one element which occurs in two given sorted arrays of integers. 


 101. Write a JavaScript program to check whether a given string contains only Latin letters and no two uppercase and no two lowercase letters are in adjacent positions. 


 102. Write a JavaScript program to find the number of inversions of a given array of integers. 
 Note: Two elements of the array a stored at positions i and j form an inversion if a[i] > a[j] and i < j.


 103. Write a JavaScript program to find the maximal number from a given positive integer by deleting exactly one digit of the given number. 


 104. Write a JavaScript program to find two elements of the array such that their absolute difference is not greater than a given integer but is as close to the said integer. 


 105. Write a JavaScript program to find the number of times to replace a given number with the sum of its digits until it convert to a single digit number. 


 106. Write a JavaScript program to divide an integer by another integer as long as the result is an integer and return the result. 


 107. Write a JavaScript program to find the number of sorted pairs formed by its elements of a given array of integers such that one element in the pair is divisible by the other one. 
 For example - The output of [1, 3, 2] ->2 - (1,3), (1,2).
 The output of [2, 4, 6] -> 2 - (2,4), (2,6)
 The output of [2, 4, 16] -> 3 - (2,4), (2,16), (4,16)


 108. Write a JavaScript program to create the dot products of two given 3D vectors. 
 Note: The dot product is the sum of the products of the corresponding entries of the two sequences of numbers.


 109. Write a JavaScript program to sort an array of all prime numbers between 1 and a given integer. 


 110. Write a JavaScript program to find the number of even values in sequence before the first occurrence of a given number. 


 111. Write a JavaScript program to check a number from three given numbers where two numbers are equal, find the third one. 


 112. Write a JavaScript program to find the number of trailing zeros in the decimal representation of the factorial of a given number. 


 113. Write a JavaScript program to calculate the sum of n + n/2 + n/4 + n/8 + .... where n is a positive integer and all divisions are integer. 


 114. Write a JavaScript program to check whether a given string represents a correct sentence or not. A string is considered correct sentence if it starts with the capital letter and ends with a full stop (.). 


 115. Write a JavaScript program to check whether a matrix is a diagonal matrix or not. In linear algebra, a diagonal matrix is a matrix in which the entries outside the main diagonal are all zero (the diagonal from the upper left to the lower right). 
 Example:
 [1, 0, 0], [0, 2, 0], [0, 0, 3] ]) = true
 [1, 0, 0], [0, 2, 3], [0, 0, 3] ]) = false


 116. Write a JavaScript program to find all the possible options to replace the hash in a string (Consists of digits and one hash (#)) with a digit to produce an integer divisible by 3. 
 For a string "2*0", the output should be : ["210", "240", "270"]


 117. Write a JavaScript program to check whether a given matrix is an identity matrix. 
 Note: In linear algebra, the identity matrix, or sometimes ambiguously called a unit matrix, of size n is the n ? n square matrix with ones on the main diagonal and zeros elsewhere.
 [[1, 0, 0], [0, 1, 0], [0, 0, 1]] -> true
 [[1, 0, 0], [0, 1, 0], [1, 0, 1]] -> false


 118. Write a JavaScript program to check whether a given number is in a given range. 


 119. Write a JavaScript program to check whether a given integer has an increasing digits sequence. 


 120. Write a JavaScript program to check whether a point lies strictly inside a given circle. 
 Input:
 Center of the circle (x, y)
 Radius of circle: r
 Point inside a circle (a, b)


 121. Write a JavaScript program to check whether a given matrix is lower triangular or not. 
 Note: A square matrix is called lower triangular if all the entries above the main diagonal are zero.


 122. Write a JavaScript program to check whether a given array of integers represents either a strictly increasing or a strictly decreasing sequence. 


 123. Write a JavaScript program to find whether the members of a given array of integers is a permutation of numbers from 1 to a given integer. 


 124. Write a JavaScript program to create the value of NOR of two given booleans. 
 Note: In boolean logic, logical nor or joint denial is a truth-functional operator which produces a result that is the negation of logical or. That is, a sentence of the form (p NOR q) is true precisely when neither p nor q is true - i.e. when both of p and q are false
 Sample Example:
 For x = true and y = false, the output should be logical_Nor(x, y) = false; For x = false and y = false, the output should be logical_Nor(x, y) = true.


 125. Write a JavaScript program to find the longest string from a given array. 


 126. Write a JavaScript program to get the largest even number from an array of integers. 


 127. Write a JavaScript program to reverse the order of the bits in a given integer. 
 56 -> 111000 after reverse 7 -> 111
 234 -> 11101010 after reverse 87 -> 1010111


 128. Write a JavaScript program to find the smallest round number that is not less than a given value. 
 Note: A round number is informally considered to be an integer that ends with one or more zeros.[3] So, 590 is rounder than 592, but 590 is less round than 600.


 129. Write a JavaScript program to find the smallest prime number strictly greater than a given number. 


 130. Write a JavaScript program to find the number of even digits in a given integer. 


 131. Write a JavaScript program to create an array of prefix sums of the given array. 
 In computer science, the prefix sum, cumulative sum, inclusive scan, or simply scan of a sequence of numbers x0, x1, x2, ... is a second sequence of numbers y0, y1, y2, ..., the sums of prefixes of the input sequence:
 y0 = x0
 y1 = x0 + x1
 y2 = x0 + x1+ x2
 ...


 132. Write a JavaScript program to find all distinct prime factors of a given integer. 


 133. Write a JavaScript program to check whether a given fraction is proper or not. 
 Note: There are two types of common fractions, proper or improper. When the numerator and the denominator are both positive, the fraction is called proper if the numerator is less than the denominator, and improper otherwise.


 134. Write a JavaScript program to change the characters (lower case) in a string where a turns into z, b turns into y, c turns into x, ..., n turns into m, m turns into n, ..., z turns into a. 


 135. Write a JavaScript program to remove all characters from a given string that appear more than once. 


 136. Write a JavaScript program to replace the first digit in a string (should contains at least digit) with $ character. 


 137. Write a JavaScript program to test whether a given integer is greater than 15 return the given number, otherwise return 15. 


 138. Write a JavaScript program to reverse the bits of a given 16 bits unsigned short integer. 


 139. Write a JavaScript program to find the position of a rightmost round number in an array of integers. Returns 0 if there are no round number.  
 Note: A round number is informally considered to be an integer that ends with one or more zeros.


 140. Write a JavaScript program to check whether all the digits in a given number are the same or not.  


 141. Write a JavaScript program to find the number of elements which presents in both of the given arrays.  


 142. Write a JavaScript program to simplify a given absolute path for a file in Unix-style.  


 143. Write a JavaScript program to sort the strings of a given array of strings in the order of increasing lengths.  
 Note: Do not change the order if the lengths of two string are same.


 144. Write a JavaScript program to break an address of an url and put it's part into an array.  
 Note: url structure : :.org[/] and there may be no part in the address.


 145. Write a JavaScript program to find the maximum integer n such that 1 + 2 + ... + n <= a given integer.  


 146. Write a JavaScript program to compute the sum of cubes of all integer from 1 to a given integer.  


 147. Write a JavaScript program to compute the sum of all digits that occur in a given string.  


 148. Write a JavaScript program to swap two halves of a given array of integers of even length.  


 149. Write a JavaScript program to change the capitalization of all letters in a given string.  


 150. Write a JavaScript program to swap pairs of adjacent digits of a given integer of even length.  




Conditional Statements and Loops.html // 1. Write a JavaScript program that accept two integers and display the larger. 


// 2. Write a JavaScript conditional statement to find the sign of product of three numbers. Display an alert box with the specified sign. 
// Sample numbers : 3, -7, 2
// Output : The sign is -


// 3. Write a JavaScript conditional statement to sort three numbers. Display an alert box to show the result. 
// Sample numbers : 0, -1, 4
// Output : 4, 0, -1


// 4. Write a JavaScript conditional statement to find the largest of five numbers. Display an alert box to show the result. 
// Sample numbers : -5, -2, -6, 0, -1
// Output : 0


// 5. Write a JavaScript for loop that will iterate from 0 to 15. For each iteration, it will check if the current number is odd or even, and display a message to the screen. 
// Sample Output :
// "0 is even"
// "1 is odd"
// "2 is even"
// ----------
// ----------


// 6. Write a JavaScript program which compute, the average marks of the following students Then, this average is used to determine the corresponding grade. 
// Student Name 	Marks
// David 	80
// Vinoth 	77
// Divya 	88
// Ishitha 	95
// Thomas 	68

// The grades are computed as follows :
// Range 	Grade
// <60 	F
// <70 	D
// <80 	C
// <90 	B
// <100 	A



// 7. Write a JavaScript program which iterates the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz". 


// 8. According to Wikipedia a happy number is defined by the following process :
// "Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers (or sad numbers)".
// Write a JavaScript program to find and print the first 5 happy numbers. 


// 9. Write a JavaScript program to find the armstrong numbers of 3 digits. 
// Note : An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself. For example, 371 is an Armstrong number since 3**3 + 7**3 + 1**3 = 371.


// 10. Write a JavaScript program to construct the following pattern, using a nested for loop. 

// *  
// * *  
// * * *  
// * * * *  
// * * * * *  



// 11. Write a JavaScript program to compute the greatest common divisor (GCD) of two positive integers. 


// 12. Write a JavaScript program to sum the multiples of 3 and 5 under 1000. 




Date.html // 1. Write a JavaScript function to check whether an `input` is a date object or not. 

// Test Data :
// console.log(is_date("October 13, 2014 11:13:00"));
// console.log(is_date(new Date(86400000)));
// console.log(is_date(new Date(99,5,24,11,33,30,0)));
// console.log(is_date([1, 2, 4, 0]));
// Output :
// false
// true
// true
// false



// 2. Write a JavaScript function to get the current date. 

// Note : Pass a separator as an argument.
// Test Data :
// console.log(curday('/'));
// console.log(curday('-'));
// Output :
// "11/13/2014"
// "11-13-2014"



// 3. Write a JavaScript function to get the number of days in a month. 

// Test Data :
// console.log(getDaysInMonth(1, 2012));
// console.log(getDaysInMonth(2, 2012));
// console.log(getDaysInMonth(9, 2012));
// console.log(getDaysInMonth(12, 2012));
// Output :
// 31
// 29
// 30
// 31



// 4. Write a JavaScript function to get the month name from a particular date. 

// Test Data :
// console.log(month_name(new Date("10/11/2009")));
// console.log(month_name(new Date("11/13/2014")));
// Output :
// "October"
// "November"



// 5. Write a JavaScript function to compare dates (i.e. greater than, less than or equal to). 

// Test Data :
// console.log(compare_dates(new Date('11/14/2013 00:00'), new Date('11/14/2013 00:00')));
// console.log(compare_dates(new Date('11/14/2013 00:01'), new Date('11/14/2013 00:00')));
// console.log(compare_dates(new Date('11/14/2013 00:00'), new Date('11/14/2013 00:01')));
// Output :
// "Date1 = Date2"
// "Date1 > Date2"
// "Date2 > Date1"



// 6. Write a JavaScript function to add specified minutes to a Date object. 

// Test Data :
// console.log(add_minutes(new Date(2014,10,2), 30).toString());
// Output :
// "Sun Nov 02 2014 00:30:00 GMT+0530 (India Standard Time)"



// 7. Write a JavaScript function to test whether a date is a weekend. 

// Note : Use standard Saturday/Sunday definition of a weekend.
// Test Data :
// console.log(is_weekend('Nov 15, 2014'));
// console.log(is_weekend('Nov 16, 2014'));
// console.log(is_weekend('Nov 17, 2014'));
// Output :
// "weekend"
// "weekend"
// undefined



// 8. Write a JavaScript function to get difference between two dates in days. 

// Test Data :
// console.log(date_diff_indays('04/02/2014', '11/04/2014'));
// console.log(date_diff_indays('12/02/2014', '11/04/2014'));
// Output :
// 216
// -28



// 9. Write a JavaScript function to get the last day of a month. 

// Test Data :
// console.log(lastday(2014,0));
// console.log(lastday(2014,1));
// console.log(lastday(2014,11));
// Output :
// 31
// 28
// 31



// 10. Write a JavaScript function to calculate 'yesterday day'. 

// Test Data :
// console.log(yesterday('Nov 15, 2014'));
// console.log(yesterday('Nov 16, 2015'));
// console.log(yesterday('Nov 17, 2016'));
// Output :
// "Fri Nov 14 2014 00:00:00 GMT+0530 (India Standard Time)"
// "Sun Nov 15 2015 00:00:00 GMT+0530 (India Standard Time)"
// "Wed Nov 16 2016 00:00:00 GMT+0530 (India Standard Time)"



// 11. Write a JavaScript function to get the maximum date from an array of dates. 

// Test Data :
// console.log(max_date(['2015/02/01', '2015/02/02', '2015/01/03']));
// Output :
// "2015/02/02"



// 12. Write a JavaScript function to get the minimum date from an array of dates. 

// Test Data :
// console.log(min_date(['2015/02/01', '2015/02/02', '2015/01/03']));
// Output :
// "2015/01/03"



// 13. Write a JavaScript function that will return the number of minutes in hours and minutes. 

// Test Data :
// console.log(timeConvert(200));
// Output :
// "200 minutes = 3 hour(s) and 20 minute(s)."



// 14. Write a JavaScript function to get the amount of days of a year. 

// Test Data :
// console.log(days_of_a_year(2015));
// 365
// console.log(days_of_a_year(2016));
// 366



// 15. Write a JavaScript function to get the quarter (1 to 4) of the year. 

// Test Data :
// console.log(quarter_of_the_year(new Date(2015, 1, 21)));
// 2
// console.log(quarter_of_the_year(new Date(2015, 10, 18)));
// 4



// 16. Write a JavaScript function to count the number of days passed since beginning of the year. 

// Test Data :
// console.log(days_passed(new Date(2015, 0, 15)));
// 15
// console.log(days_passed(new Date(2015, 11, 14)));
// 348



// 17. Write a JavaScript function to convert a Unix timestamp to time. 

// Test Data :
// console.log(days_passed(new Date(2015, 0, 15)));
// 15
// console.log(days_passed(new Date(2015, 11, 14)));
// 348



// 18. Write a JavaScript program to calculate age. 

// Test Data :
// console.log(calculate_age(new Date(1982, 11, 4)));
// 32
// console.log(calculate_age(new Date(1962, 1, 1)));
// 53



// 19. Write a JavaScript function to get the day of the month, 2 digits with leading zeros. 
// Test Data :
// d= new Date(2015, 10, 1);
// console.log(day_of_the_month(d));
// "01"



// 20. Write a JavaScript function to get a textual representation of a day (three letters, Mon through Sun). 
// Test Data :
// dt = new Date(2015, 10, 1);
// console.log(short_Days(dt));
// "Sun"



// 21. Write a JavaScript function to get a full textual representation of the day of the week (Sunday through Saturday). 
// Test Data :
// dt = new Date(2015, 10, 1);
// console.log(long_Days(dt));
// "Sunday"



// 22. Write a JavaScript function to get ISO-8601 numeric representation of the day of the week (1 (for Monday) to 7 (for Sunday)). 
// Test Data :
// dt = new Date(2015, 10, 1);
// console.log(ISO_numeric_date(dt));
// 7



// 23. Write a JavaScript function to get English ordinal suffix for the day of the month, 2 characters (st, nd, rd or th.). 
// Test Data :
// dt = new Date(2015, 10, 1);
// console.log(english_ordinal_suffix(dt));
// "1st"



// 24. Write a JavaScript function to get ISO-8601 week number of year, weeks starting on Monday. 
// Example : 42 (the 42nd week in the year)
// Test Data :
// dt = new Date(2015, 10, 1);
// console.log(ISO8601_week_no(dt));
// 44



// 25. Write a JavaScript function to get a full textual representation of a month, such as January or June. 
// Test Data :
// dt = new Date(2015, 10, 1);
// console.log(full_month(dt));
// "November"



// 26. Write a JavaScript function to get a numeric representation of a month, with leading zeros (01 through 12). 
// Test Data :
// dt = new Date(2015, 10, 1);
// console.log(numeric_month(dt));
// "11"



// 27. Write a JavaScript function to get a short textual representation of a month, three letters (Jan through Dec). 
// Test Data :
// dt = new Date(2015, 10, 1);
// console.log(short_months(dt));
// "Nov"



// 28. Write a JavaScript function to get a full numeric representation of a year (4 digits). 
// Test Data :
// dt = new Date(2015, 10, 1);
// console.log(full_year(dt));
// 2015



// 29. Write a JavaScript function to get a two digit representation of a year. 
// Examples : 79 or 04
// Test Data :
// dt = new Date(1989, 10, 1);
// console.log(sort_year(dt));
// "89"



// 30. Write a JavaScript function to get lowercase Ante meridiem and Post meridiem. 


// 31. Write a JavaScript function to get uppercase Ante meridiem and Post meridiem. 



// 32. Write a JavaScript function to swatch Internet time (000 through 999). 
// Test Data :
// dt = new Date(1989, 10, 1);
// console.log(internet_time(dt));
// 812



// 33. Write a JavaScript function to get 12-hour format of an hour with leading zeros. 
// Test Data :
// dt = new Date(1989, 10, 1);
// console.log(hours_with_zeroes(dt));
// "12"



// 34. Write a JavaScript function to get 24-hour format of an hour without leading zeros. 
// Test Data :
// dt = new Date(1989, 10, 1);
// console.log(hours_without_zeroes(dt));
// 0



// 35. Write a JavaScript function to get minutes with leading zeros (00 to 59). 
// Test Data :
// dt = new Date(1989, 10, 1);
// console.log(minutes_with_leading_zeros(dt));
// "00"



// 36. Write a JavaScript function to get seconds with leading zeros (00 through 59). 
// Test Data :
// dt = new Date(1989, 10, 1);
// console.log(seconds_with_leading_zeros(dt));
// "00"



// 37. Write a JavaScript function to get Timezone. 
// Test Data :
// dt = new Date();
// console.log(seconds_with_leading_zeros(dt));
// "India Standard Time"


// 38. Write a JavaScript function to find whether or not the date is in daylights savings time. 
// Test Data :
// dt = new Date();
// console.log(daylights_savings(dt));
// 1



// 39. Write a JavaScript function to get difference to Greenwich time (GMT) in hours. 
// Test Data :
// dt = new Date();
// console.log(diff_to_GMT(dt));
// "+05.500"



// 40. Write a JavaScript function to get timezone offset in seconds. 
// Note : The offset for timezones west of UTC is always negative, and for those east of UTC is always positive.
// Test Data :
// dt = new Date();
// console.log(timezone_offset_in_seconds(dt));
// 19800



// 41. Write a JavaScript function to add specified years to a date. 
// Test Data :
// dt = new Date(2014,10,2);
// console.log(add_years(dt, 10).toString());
// Output :
// "Sat Nov 02 2024 00:00:00 GMT+0530 (India Standard Time)"



// 42. Write a JavaScript function to add specified weeks to a date. 
// Test Data :
// dt = new Date(2014,10,2);
// console.log(add_weeks(dt, 10).toString());
// Output :
// "Sun Jan 11 2015 00:00:00 GMT+0530 (India Standard Time)"



// 43. Write a JavaScript function to add specified months to a date. 
// Test Data :
// dt = new Date(2014,10,2);
// console.log(add_months(dt, 10).toString());
// Output :
// "Wed Sep 02 2015 00:00:00 GMT+0530 (India Standard Time)"



// 44. Write a JavaScript function to get time differences in minutes between two dates. 
// Test Data :
// dt1 = new Date("October 13, 2014 11:11:00");
// dt2 = new Date("October 13, 2014 11:13:00");
// console.log(diff_minutes(dt1, dt2));
// 2



// 45. Write a JavaScript function to get time differences in hours between two dates. 
// Test Data :
// dt1 = new Date("October 13, 2014 08:11:00");
// dt2 = new Date("October 13, 2014 11:13:00");
// console.log(diff_hours(dt1, dt2));
// 3



// 46. Write a JavaScript function to get time differences in days between two dates. 
// Test Data :
// dt1 = new Date("October 13, 2014 08:11:00");
// dt2 = new Date("October 19, 2014 11:13:00");
// console.log(diff_days(dt1, dt2));
// 6



// 47. Write a JavaScript function to get time differences in weeks between two dates. 
// Test Data :
// dt1 = new Date("June 13, 2014 08:11:00");
// dt2 = new Date("October 19, 2014 11:13:00");
// console.log(diff_weeks(dt1, dt2));
// 18



// 48. Write a JavaScript function to get time differences in months between two dates. 
// Test Data :
// dt1 = new Date("June 13, 2014 08:11:00");
// dt2 = new Date("October 19, 2014 11:13:00");
// console.log(diff_months(dt1, dt2));
// 5



// 49. Write a JavaScript function to get time differences in years between two dates. 
// Test Data :
// dt1 = new Date("June 13, 2014 08:11:00");
// dt2 = new Date("October 19, 2017 11:13:00");
// console.log(diff_years(dt1, dt2));
// 3



// 50. Write a JavaScript function to get the week start date. 


// 51. Write a JavaScript function to get the week end date. 


// 52. Write a JavaScript function to get the month start date. 


// 53. Write a JavaScript function to get the month end date. 




Drawing.html // 1. Write a JavaScript program to draw the following rectangular shape.
// Expected Output :
// rectagular shape


// 2. Write a JavaScript program to draw a circle.
// Expected Output :
// draw a circle


// 3. Write a JavaScript program to draw two intersecting rectangles, one of which has alpha transparency.
// Expected Output :
// intersecting rectangles


// 4. Write a JavaScript program to draw the following right-angled triangle.
// Expected Output :
// right angled triangle


// 5. Write a JavaScript program to draw the following diagram [use moveto() function].
// Expected Output :
// draw fun


// 6. Write a JavaScript program to draw the following diagram [diagonal, white to black circles].
// Expected Output :
// diagonal, white to black circles




Functions.html // 1. Write a JavaScript function that reverse a number. 
// Example x = 32243;
// Expected Output : 34223


// 2. Write a JavaScript function that checks whether a passed string is palindrome or not? 
// A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.


// 3. Write a JavaScript function that generates all combinations of a string. 
// Example string : 'dog'
// Expected Output : d,do,dog,o,og,g


// 4. Write a JavaScript function that returns a passed string with letters in alphabetical order. 
// Example string : 'webmaster'
// Expected Output : 'abeemrstw'
// Assume punctuation and numbers symbols are not included in the passed string.


// 5. Write a JavaScript function that accepts a string as a parameter and converts the first letter of each word of the string in upper case. 
// Example string : 'the quick brown fox'
// Expected Output : 'The Quick Brown Fox '


// 6. Write a JavaScript function that accepts a string as a parameter and find the longest word within the string. 
// Example string : 'Web Development Tutorial'
// Expected Output : 'Development'


// 7. Write a JavaScript function that accepts a string as a parameter and counts the number of vowels within the string. 
// Note : As the letter 'y' can be regarded as both a vowel and a consonant, we do not count 'y' as vowel here.
// Example string : 'The quick brown fox'
// Expected Output : 5


// 8. Write a JavaScript function that accepts a number as a parameter and check the number is prime or not. 
// Note : A prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.


// 9. Write a JavaScript function which accepts an argument and returns the type. 
// Note : There are six possible values that typeof returns: object, boolean, function, number, string, and undefined.


// 10. Write a JavaScript function which returns the n rows by n columns identity matrix. 


// 11. Write a JavaScript function which will take an array of numbers stored and find the second lowest and second greatest numbers, respectively. 
// Sample array : [1,2,3,4,5]
// Expected Output : 2,4
// .

// 12. Write a JavaScript function which says whether a number is perfect. 
// According to Wikipedia : In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors, that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum). Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself).
// Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.
// .

// 13. Write a JavaScript function to compute the factors of a positive integer. 
// .

// 14. Write a JavaScript function to convert an amount to coins. 
// Sample function : amountTocoins(46, [25, 10, 5, 2, 1])
// Here 46 is the amount. and 25, 10, 5, 2, 1 are coins.
// Output : 25, 10, 10, 1
// .

// 15. Write a JavaScript function to compute the value of bn where n is the exponent and b is the bases. Accept b and n from the user and display the result. 
// .

// 16. Write a JavaScript function to extract unique characters from a string. 
// Example string : "thequickbrownfoxjumpsoverthelazydog"
// Expected Output : "thequickbrownfxjmpsvlazydg"
// .

// 17. Write a JavaScript function to  get the number of occurrences of each letter in specified string. 
// .

// 18. Write a function for searching JavaScript arrays with a binary search. 
// Note : A binary search searches by splitting an array into smaller and smaller chunks until it finds the desired value.
// .

// 19. Write a JavaScript function that returns array elements larger than a number. 
// .

// 20. Write a JavaScript function that generates a string id (specified length) of random characters. 
// Sample character list : "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
// .

// 21. Write a JavaScript function to get all possible subset with a fixed length (for example 2) combinations in an array. 
// Sample array : [1, 2, 3] and subset length is 2
// Expected output : [[2, 1], [3, 1], [3, 2], [3, 2, 1]]
// .

// 22. Write a JavaScript function that accepts two arguments, a string and a letter and the function will count the number of occurrences of the specified letter within the string. 
// Sample arguments : 'w3resource.com', 'o'
// Expected output : 2


// 23. Write a JavaScript function to find the first not repeated character. 
// Sample arguments : 'abacddbec'
// Expected output : 'e'


// 24. Write a JavaScript function to apply Bubble Sort algorithm. 
// Note : According to wikipedia "Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that works by repeatedly stepping through the list to be sorted, comparing each pair of adjacent items and swapping them if they are in the wrong order".
// Sample array : [12, 345, 4, 546, 122, 84, 98, 64, 9, 1, 3223, 455, 23, 234, 213]
// Expected output : [3223, 546, 455, 345, 234, 213, 122, 98, 84, 64, 23, 12, 9, 4, 1]


// 25. Write a JavaScript function that accept a list of country names as input and returns the longest country name as output. 
// Sample function : Longest_Country_Name(["Australia", "Germany", "United States of America"])
// Expected output : "United States of America"


// 26. Write a JavaScript function to find longest substring in a given a string without repeating characters. 


// 27. Write a JavaScript function that returns the longest palindrome in a given string. 

// Note: According to Wikipedia "In computer science, the longest palindromic substring or longest symmetric factor problem is the problem of finding a maximum-length contiguous substring of a given string that is also a palindrome. For example, the longest palindromic substring of "bananas" is "anana". The longest palindromic substring is not guaranteed to be unique; for example, in the string "abracadabra", there is no palindromic substring with length greater than three, but there are two palindromic substrings with length three, namely, "aca" and "ada".
// In some applications it may be necessary to return all maximal palindromic substrings (that is, all substrings that are themselves palindromes and cannot be extended to larger palindromic substrings) rather than returning only one substring or returning the maximum length of a palindromic substring.


// 28. Write a JavaScript program to pass a 'JavaScript function' as parameter. 


// 29. Write a JavaScript function to get the function name. 




Fundamentals (ES6).html 1. Write a JavaScript program to compare two objects to determine if the first one contains equivalent property values to the second one. 



2. Write a JavaScript program to copy a string to the clipboard. 



3. Write a JavaScript program to converts a comma-separated values (CSV) string to a 2D array. 



4. Write a JavaScript program to convert a comma-separated values (CSV) string to a 2D array of objects. The first row of the string is used as the title row. 



5. Write a JavaScript program to convert an array of objects to a comma-separated values (CSV) string that contains only the columns specified. 



6. Write a JavaScript program to target a given value in a nested JSON object, based on the given key. 



7. Write a JavaScript program to converts a specified number to an array of digits. 



8. Write a JavaScript program to filter out the specified values from a specified array. Return the original array without the filtered values. 



9. Write a JavaScript program to combine the numbers of a given array into an array containing all combinations. 



10. Write a JavaScript program to extract out the values at the specified indexes from a specified array. 



11. Write a JavaScript program to generate a random hexadecimal color code. 



12. Write a JavaScript program to removes non-printable ASCII characters from a given string. 



13. Write a JavaScript program to convert the length of a given string in bytes. 



14. Write a JavaScript program to replace the names of multiple object keys with the values provided. 



15. Write a JavaScript program to return the minimum-maximum value of an array, after applying the provided function to set comparing rule. 



16. Write a JavaScript function that returns true if the provided predicate function returns true for all elements in a collection, false otherwise. 



17. Write a JavaScript program to split values of two given arrays into two groups. If an element in filter is truthy, the corresponding element in the collection belongs to the first group; otherwise, it belongs to the second group. 



18. Write a JavaScript program to remove specified elements from the left of a given array of elements. 



19. Write a JavaScript program to remove specified elements from the right of a given array of elements. 



20. Write a JavaScript program to extend a 3-digit color code to a 6-digit color code. 



21. Write a JavaScript program to get every nth element in a given array. 



22. Write a JavaScript program to filter out the non-unique values in an array. 



23. Write a JavaScript program to filter out the non-unique values in an array, based on a provided comparator function. 



24. Write a JavaScript program to dcapitalize the first letter of a string. 



25. Write a JavaScript program to create a new array out of the two supplied by creating each possible pair from the arrays. 



26. Write a JavaScript program that will return true if the string is y/yes or false if the string is n/no. 



27. Write a JavaScript program to find every element that exists in any of the two given arrays once, using a provided comparator function. 



28. Write a JavaScript program to measure the time taken by a function to execute. 



29. Write a JavaScript program to convert a value to a safe integer. 



30. Write a JavaScript program to filter out the element(s) of a given array, that have one of the specified values. 



31. Write a JavaScript program to find all elements in a given array except for the first one. Return the whole array if the array's length is 1. 



32. Write a JavaScript program to get the sum of a given array, after mapping each element to a value using the provided function. 



33. Write a JavaScript program to get a random number in the specified range. 



34. Write a JavaScript program to get a random integer in the specified range. 



35. Write a JavaScript program to get an array of given n random integers in the specified range. 



36. Write a JavaScript program to create a function that invokes each provided function with the arguments it receives and returns the results. 



37. Write a JavaScript program to get a sorted array of objects ordered by properties and orders. 



38. Write a JavaScript program to pad a string on both sides with the specified character, if it's shorter than the specified length. 



39. Write a JavaScript program to remove the key-value pairs corresponding to the given keys from an object. 



40. Write a JavaScript program to create an array of key-value pair arrays from a given object. 



41. Write a JavaScript program to create an object from the given key-value pairs. 



42. Write a JavaScript program to get a customized coalesce function that returns the first argument that returns true from the provided argument validation function. 



43. Write a JavaScript program to change function that accepts an array into a variadic function. 



44. Write a JavaScript program to remove falsey values from a given array. 



45. Write a JavaScript program to split values into two groups, if an element in filter is truthy, the corresponding element in the collection belongs to the first group; otherwise, it belongs to the second group. 



46. Write a JavaScript program to curry (curries) a function. 



47. Write a JavaScript program to perform a deep comparison between two values to determine if they are equivalent. 



48. Write a JavaScript program to get an array of function property names from own (and optionally inherited) enumerable properties of an object. 



49. Write a JavaScript program to retrieve a set of properties indicated by the given selectors from an object. 



50. Write a JavaScript program to convert an integer to a suffixed string, adding am or pm based on its value. 



51. Write a JavaScript program to get an object containing the parameters of the current URL. 



52. Write a JavaScript program to group the elements of a given array based on the given function. 



53. Write a JavaScript program to Initialize a two dimension array of given width and height and value. 



54. Write a JavaScript program to initialize an array containing the numbers in the specified range where start and end are inclusive with their common difference step.



55. Write a JavaScript program to Join all given URL segments together, then normalizes the resulting URL. 



56. Write a JavaScript program to check whether all elements in a given array are equal or not. 



57. Write a JavaScript program to compute the average of an array, after mapping each element to a value using the provided function. 



58. Write a JavaScript program to split values into two groups according to a predicate function, which specifies which group an element in the input collection belongs to. 



59. Write a JavaScript program to create a function that invokes fn with a given context, optionally adding any additional supplied parameters to the beginning of the arguments. 



60. Write a JavaScript program to create a function that invokes the method at a given key of an object, optionally adding any additional supplied parameters to the beginning of the arguments. 



61. Write a JavaScript program to cast the provided value as an array if it's not one. 



62. Write a JavaScript program to chain asynchronous functions. 



63. Write a JavaScript program to clone a given regular expression. 



64. Write a JavaScript program to get the first non-null / undefined argument. 



65. Write a JavaScript program to add special characters to text to print in color in the console (combined with console.log()). 



66. Write a JavaScript program to perform right-to-left function composition. 



67. Write a JavaScript program to perform left-to-right function composition. 



68. Write a JavaScript program that accepts a converging function and a list of branching functions and returns a function that applies each branching function to the arguments and the results of the branching functions are passed as arguments to the converging function. 



69. Write a JavaScript program to group the elements of an array based on the given function and returns the count of elements in each group. 



70. Write a JavaScript program to count the occurrences of a value in an array. 



71. Write a JavaScript program to create a deep clone of an object. 



72. Write a JavaScript program to detect whether the website is being opened in a mobile device or a desktop/laptop. 



73. Write a JavaScript program to return the difference between two arrays, after applying the provided function to each array element of both. 



74. Write a JavaScript program to filter out all values from an array for which the comparator function does not return true. 



75. Write a JavaScript program to compute the new ratings between two or more opponents using the Elo rating system. It takes an array of pre-ratings and returns an array containing post-ratings. The array should be ordered from best performer to worst performer (winner -> loser). 



76. Write a JavaScript program to execute a provided function once for each array element, starting from the array's last element.



77. Write a JavaScript program to iterate over all own properties of an object, running a callback for each one. 



78. Write a JavaScript program to invert the key-value pairs of an object, without mutating it. The corresponding inverted value of each inverted key is an array of keys responsible for generating the inverted value. If a function is supplied, it is applied to each inverted key. 



79. Write a JavaScript program to take any number of iterable objects or objects with a length property and returns the longest one. 



80. Write a JavaScript program to implement the Luhn Algorithm used to validate a variety of identification numbers, such as credit card numbers, IMEI numbers, National Provider Identifier numbers etc. 



81. Write a JavaScript program to create an object with keys generated by running the provided function for each key and the same values as the provided object. 



82. Write a JavaScript program to map the values of an array to an object using a function, where the key-value pairs consist of the original value as the key and the mapped value. 



83. Write a JavaScript program to create a new string with the results of calling a provided function on every character in the calling string. 



84. Write a JavaScript program to create an object with the same keys as the provided object and values generated by running the provided function for each value. 



85. Write a JavaScript program to replace all but the last number of characters with the specified mask character. 



86. Write a JavaScript program to get the maximum value of an array, after mapping each element to a value using the provided function. 



87. Write a JavaScript program to get the n maximum elements from the provided array. If n is greater than or equal to the provided array's length, then return the original array(sorted in descending order). 



88. Write a JavaScript program to get the median of an array of numbers. 



89. Write a JavaScript program to negates a predicate function.



90. Write a JavaScript program to nest a given flat array of objects linked to one another recursively. 



91. Write a JavaScript program that will return true if the provided predicate function returns false for all elements in a collection, false otherwise. 



92. Write a JavaScript program to create a function that gets the argument at index n. If n is negative, the nth argument from the end is returned. 



93. Write a JavaScript program to remove an event listener from an element. 



94. Write a JavaScript program to move the specified amount of elements to the end of the array. 



95. Write a JavaScript program to add an event listener to an element with the ability to use event delegation. 



96. Write a JavaScript program to pick the key-value pairs corresponding to the given keys from an object. 



97. Write a JavaScript program to create an object composed of the properties the given function returns truthy for. The function is invoked with two arguments: (value, key). 



98. Write a JavaScript program to filter an array of objects based on a condition while also filtering out unspecified keys. 



99. Write a JavaScript program to hash a given input string into a whole number. 



100. Write a JavaScript program to create an array of elements, grouped based on the position in the original arrays and using function as the last value to specify how grouped values should be combined. 



101. Write a JavaScript program to return the object associating the properties to the values of a given array of valid property identifiers and an array of values. 



102. Write a JavaScript program to create an array of elements, grouped based on the position in the original arrays. 



103. Write a JavaScript program to convert a given string into an array of words. 



104. Write a JavaScript program to test a value, x, against a predicate function. If true, return fn(x). Else, return x. 



105. Write a JavaScript program that return true if the given value is a number, false otherwise. 



106. Write a JavaScript program to create an array of elements, ungrouping the elements in an array produced by zip and applying the provided function. 



107. Write a JavaScript program to get all unique values (form the right side of the array) of an array, based on a provided comparator function.



108. Write a JavaScript program to get all unique values of an array, based on a provided comparator function. 



109. Write a JavaScript program to get the nth element of a given array. 



110. Write a JavaScript program to get every element that exists in any of the two arrays once. 



111. Write a JavaScript program to build an array, using an iterator function and an initial seed value. 



112. Write a JavaScript program to unflatten an object with the paths for keys. 



113. Write a JavaScript program to unescape escaped HTML characters. 



114. Write a JavaScript program to uncurry a function up to depth n. 



115. Write a JavaScript program to create a function that accepts up to one argument, ignoring any additional arguments.



116. Write a JavaScript program to check if the predicate (second argument) is truthy on all elements of a collection (first argument). 



117. Write a JavaScript program to truncate a string up to a specified length. 



118. Write a JavaScript program to apply a function against an accumulator and each key in the object (from left to right). 



119. Write a JavaScript program to create tomorrow's date in a string representation. 



120. Write a JavaScript program to convert a string to snake case. 



121. Write a JavaScript program to convert a value to a safe integer. 



122. Write a JavaScript program to add an ordinal suffix to a number. 



123. Write a JavaScript program to convert a string to kebab case. 



124. Write a JavaScript program to reduce a given Array-like into a value hash (keyed data store). 



125. Write a JavaScript program to convert a float-point arithmetic to the Decimal mark form and It will make a comma separated string from a number. 



126. Write a JavaScript program to create a specified currency formatting from a given number. 



127. Write a JavaScript program to Iterate over a callback n times. 



128. Write a JavaScript program to get removed elements of a given array until the passed function returns true. 



129. Write a JavaScript program to get removed elements from the end of a given array until the passed function returns true. 



130. Write a JavaScript program to remove n elements from the end of a given array. 



131. Write a JavaScript program to get an array with n elements removed from the beginning from a given array 



132. Write a JavaScript program to get the symmetric difference between two given arrays, using a provided function as a comparator. 



133. Write a JavaScript program to get the symmetric difference between two given arrays, after applying the provided function to each array element of both. 



134. Write a JavaScript program to get the symmetric difference between two given arrays. 



135. Write a JavaScript program to get the sum of the powers of all the numbers from start to end (both inclusive). 



136. Write a JavaScript program to generate all permutations of a string (contains duplicates).



137. Write a JavaScript program to perform stable sorting of an array, preserving the initial indexes of items when their values are the same. Do not mutate the original array, but returns a new array instead. 



138. Write a JavaScript program that takes a variadic function and returns a closure that accepts an array of arguments to map to the inputs of the function. 



139. Write a JavaScript program to split a multiline string into an array of lines. 



140. Write a JavaScript program to get the highest index at which value should be inserted into array in order to maintain its sort order, based on a provided iterator function. 



141. Write a JavaScript program to get the highest index at which value should be inserted into array in order to maintain its sort order. 



142. Write a JavaScript program to get the lowest index at which value should be inserted into array in order to maintain its sort order.



143. Write a JavaScript program to sort the characters of a string Alphabetically. 



144. Write a JavaScript program to get an array of elements that appear in both arrays. 



145. Write a JavaScript program to randomize the order of the values of an array, returning a new array.



146. Write a JavaScript program to create a shallow clone of an object. 



147. Write a JavaScript program to serialize a cookie name-value pair into a Set-Cookie header string. 



148. Write a JavaScript program to hash the input string into a whole number. 



149. Write a JavaScript program to get a random element from an array. 



150. Write a JavaScript program to run a given array of promises in series. 





HTML DOM.html // 1. Here is a sample html file with a submit button. Now modify the style of the paragraph text through javascript code.
// Sample HTML file :

// <!DOCTYPE html>
// <html>
// <head>
// <meta charset=utf-8 />
// <title>JS DOM paragraph style</title>
// </head> 
// <body>
// <p id ='text'>JavaScript Exercises - w3resource</p> 
// <div>
// <button id="jsstyle"
// onclick="js_style()">Style</button>
// </div>
// </body>
// </html>

// Clicking on the button the font, font size, and color of the paragraph text will be changed.


// 2. Write a JavaScript function to get the values of First and Last name of the following form.
// Sample HTML file :

// <!DOCTYPE html>
// <html><head>
// <meta charset=utf-8 />
// <title>Return first and last name from a form - w3resource</title>
// </head><body>
// <form id="form1" onsubmit="getFormvalue()">
// First name: <input type="text" name="fname" value="David"><br>
// Last name: <input type="text" name="lname" value="Beckham"><br>
// <input type="submit" value="Submit">
// </form>
// </body>
// </html>



// 3. Write a JavaScript program to set the background color of a paragraph.


// 4. Here is a sample html file with a submit button. Write a JavaScript function to get the value of the href, hreflang, rel, target, and type attributes of the specified link.

// <!DOCTYPE html>
// <html><head>
// <meta charset=utf-8 />
// </head>
// <body>
// <p><a id="w3r" type="text/html" hreflang="en-us" rel="nofollow" target="_self" href="https://www.w3resource.com/">w3resource</a></p>
// <button onclick="getAttributes()">Click here to get  attributes value</button>
// </body></html>



// 5. Write a JavaScript function to add rows to a table.
// Sample HTML file :

// <!DOCTYPE html>
// <html><head>
// <meta charset=utf-8 />
// <title>Insert row in a table - w3resource</title>
// </head><body>
// <table id="sampleTable" border="1">
// <tr><td>Row1 cell1</td>
// <td>Row1 cell2</td></tr>
// <tr><td>Row2 cell1</td>
// <td>Row2 cell2</td></tr>
// </table><br>
// <input type="button" onclick="insert_Row()" value="Insert row"> 
// </body></html>



// 6. Write a JavaScript function that accept row, column, (to identify a particular cell) and a string to update the content of that cell.
// Sample HTML file :

// <!DOCTYPE html>
// <html><head>
// <meta charset=utf-8 />
// <title>Change the content of a cell</title>
// </head><body>
// <table id="myTable" border="1">
// <tr><td>Row1 cell1</td>
// <td>Row1 cell2</td></tr>
// <tr><td>Row2 cell1</td>
// <td>Row2 cell2</td></tr>
// <tr><td>Row3 cell1</td>
// <td>Row3 cell2</td></tr>
// </table><form>
// <input type="button" onclick="changeContent()" value="Change content">
// </form></body></html>



// 7. Write a JavaScript function that creates a table, accept row, column numbers from the user, and input row-column number as content (e.g. Row-0 Column-0) of a cell.
// Sample HTML file :

// <!DOCTYPE html>
// <html>
// <head>
// <meta charset=utf-8 />
// <title>Change the content of a cell</title>
// <style type="text/css">
// body {margin: 30px;}
// </style>  
// </head><body>
// <table id="myTable" border="1">
// </table><form>
// <input type="button" onclick="createTable()" value="Create the table">
// </form></body></html>



// 8. Write a JavaScript program to remove items from a dropdown list.
// Sample HTML file :

// <!DOCTYPE html>
// <html><head>
// <meta charset=utf-8 />
// <title>Remove items from a dropdown list</title>
// </head><body><form>
// <select id="colorSelect">
// <option>Red</option>
// <option>Green</option>
// <option>White</option>
// <option>Black</option>
// </select>
// <input type="button" onclick="removecolor()" value="Select and Remove">
// </form></body></html>



// 9. Write a JavaScript program to count and display the items of a dropdown list, in an alert window.
// Sample HTML file :

// <!DOCTYPE html>
// <html><head>
// <meta charset=utf-8 />
// <style type="text/css">
// body {margin: 30px;}
// </style>   
// <title>Count and display items of a dropdown list - w3resource</title>
// </head><body><form>
// Select your favorite Color :
// <select id="mySelect">
// <option>Red</option>
// <option>Green</option>
// <option>Blue</option>
// <option>White</option>
// </select>
// <input type="button" onclick="getOptions()" value="Count and Output all items">
// </form></body></html>



// 10. Write a JavaScript program to calculate the volume of a sphere.
// Sample Output of the form :

// volume sphere html form



// 11. Write a JavaScript program to display a random image (clicking on a button) from the following list.
// Sample Image information :

// "http://farm4.staticflickr.com/3691/11268502654_f28f05966c_m.jpg", width: "240", height: "160"
// "http://farm1.staticflickr.com/33/45336904_1aef569b30_n.jpg", width: "320", height: "195"
// "http://farm6.staticflickr.com/5211/5384592886_80a512e2c9.jpg", width: "500", height: "343"



// 12. Write a JavaScript program to highlight the bold words of the following paragraph, on mouse over a certain link.
// Sample link and text :
// [On mouse over here bold words of the following paragraph will be highlighted]
// We have just started this section for the users (beginner to intermediate) who want to work with various JavaScript problems and write scripts online to test their JavaScript skill.


// 13. Write a JavaScript program to get the width and height of the window (any time the window is resized).
//  



Math.html // 1. Write a JavaScript function to convert a number from one base to another. 
// Note : Both bases must be between 2 and 36.
// Test Data :
// console.log(base_convert('E164',16,8));
// console.log(base_convert(1000,2,8));
// "160544"
// "10"


// 2. Write a JavaScript function to convert a binary number to a decimal number. 
// Test Data :
// console.log(bin_to_dec('110011'));
// console.log(bin_to_dec('100'));
// 51
// 4


// 3. Write a JavaScript function to convert a decimal number to binary, hexadecimal or octal number. 
// Test Data :
// console.log(dec_to_bho(120,'B'));
// console.log(dec_to_bho(120,'H'));
// console.log(dec_to_bho(120,'O'));
// "1111000"
// "78"
// "170"


// 4. Write a JavaScript function to generate a random integer. 
// Test Data :
// console.log(rand(20,1));
// console.log(rand(1,10));
// console.log(rand(6));
// console.log(rand());
// 15
// 5
// 1
// 0


// 5. Write a JavaScript function to format a number up to specified decimal places. 
// Test Data :
// console.log(decimals(2.100212, 2));
// console.log(decimals(2.100212, 3));
// console.log(decimals(2100, 2));
// "2.10"
// "2.100"
// "2100.00"


// 6. Write a JavaScript function to find the highest value in an array. 
// Test Data :
// console.log(max([12,34,56,1]));
// console.log(max([-12,-34,0,-56,-1]));
// 56
// 0


// 7. Write a JavaScript function to find the lowest value in an array. 
// Test Data :
// console.log(min([12,34,56,1]));
// console.log(min([-12,-34,0,-56,-1]));
// 1
// -56


// 8. Write a JavaScript function to get the greatest common divisor (gcd) of two integers. 
// Note :
// According to Wikipedia - In mathematics, the greatest common divisor (gcd) of two or more integers, when at least one of them is not zero, is the largest positive integer that divides the numbers without a remainder. For example, the GCD of 8 and 12 is 4.

// Test Data :
// console.log(gcd_two_numbers(12, 13));
// console.log(gcd_two_numbers(9, 3));
// Output :
// 1
// 3


// 9. Write a JavaScript function to find the GCD (greatest common divisor) of more than 2 integers. 
// Test Data :
// console.log(gcd_more_than_two_numbers([3,15,27]));
// console.log(gcd_more_than_two_numbers([5,10,15,25]));
// Output :
// 3
// 5


// 10. Write a JavaScript function to get the least common multiple (LCM) of two numbers. 
// Note :
// According to Wikipedia - A common multiple is a number that is a multiple of two or more integers. The common multiples of 3 and 4 are 0, 12, 24, .... The least common multiple (LCM) of two numbers is the smallest number (not zero) that is a multiple of both.
// Test Data :
// console.log(lcm_two_numbers(3,15));
// console.log(lcm_two_numbers(10,15));
// Output :
// 15
// 30


// 11. Write a JavaScript function to get the least common multiple (LCM) of more than 2 integers. 
// Test Data :
// console.log(lcm_more_than_two_numbers([100,90,80,7]));
// console.log(lcm_more_than_two_numbers([5,10,15,25]));
// Output :
// 25200
// 150


// 12. Write a JavaScript function to find out if a number is a natural number or not. 
// Note :
// Natural numbers are whole numbers from 1 upwards : 1, 2, 3, and so on ... or from 0 upwards in some area of mathematics: 0, 1, 2, 3 and so on ...
// No negative numbers and no fractions.
// Test Data :
// console.log(is_Natural(-15));
// console.log(is_Natural(1));
// console.log(is_Natural(10.22));
// console.log(is_Natural(10/0));
// Output :
// false
// true
// false
// false


// 13. Write a JavaScript function to test if a number is a power of 2. 
// Test Data :
// console.log(power_of_2(16));
// console.log(power_of_2(18));
// console.log(power_of_2(256));
// Output :
// true
// false
// true


// 14. Write a JavaScript function to round a number to a given decimal places. 
// Test Data :
// console.log(precise_round(12.375,2));
// console.log(precise_round(12.37499,2));
// console.log(precise_round(-10.3079499, 3));
// Output :
// "12.38"
// "12.37"
// "-10.308"


// 15. Write a JavaScript function to check whether a value is an integer or not. 
// Note : Integer - A number which is not a fraction; a whole number.
// Test Data :
// console.log(is_Int(23));
// console.log(is_Int(4e2));
// console.log(is_Int(NaN));
// console.log(is_Int(23.75));
// console.log(is_Int(-23));
// Output :
// true
// true
// false
// false
// true


// 16. Write a JavaScript function to check to check whether a variable is numeric or not. 
// Test Data :
// console.log(is_Numeric(12));
// console.log(is_Numeric('abcd'));
// console.log(is_Numeric('12'));
// console.log(is_Numeric(' '));
// console.log(is_Numeric(1.20));
// console.log(is_Numeric(-200));
// Output :
// true
// false
// true
// false
// true
// true


// 17. Write a JavaScript function to calculate the sum of values in an array. 
// Test Data :
// console.log(sum([1,2,3]));
// console.log(sum([100,-200,3]));
// console.log(sum([1,2,'a',3]));
// Output :
// 6
// -97
// 6


// 18. Write a JavaScript function to calculate the product of values in an array. 
// Test Data :
// console.log(product([1,2,3]));
// console.log(product([100,-200,3]));
// console.log(product([1,2,'a',3]));
// Output :
// 6
// -60000
// 6


// 19. Create a Pythagorean function in JavaScript. 
// Note : The Pythagorean Theorem tells us that the relationship in every right triangle is : c2 = a2 + b2, where c is the hypotenuse and a, b are two legs of the triangle.
// Test Data :
// console.log(pythagorean_theorem(2, 4));
// console.log(pythagorean_theorem(3, 4));
// Output :
// 4.47213595499958
// 5


// 20. Write a JavaScript program to evaluate binomial coefficients. 
// Note :
// Binomial coefficient : According to Wikipedia - In mathematics, binomial coefficients are a family of positive integers that occur as coefficients in the binomial theorem. They are indexed by two nonnegative integers; the binomial coefficient indexed by n and k. Under suitable circumstances the value of the coefficient is given by the expression :
// binomial coefficients
// Arranging binomial coefficients into rows for successive values of n, and in which k ranges from 0 to n, gives a triangular array called Pascal's triangle.

// Test Data :
// console.log(binomial(8,3));
// console.log(binomial(10,2));
// Output :
// 56
// 45



// 21. Write a JavaScript function that Convert an integer into a Roman Numeral in javaScript. 



// 22. Write a JavaScript function that Convert Roman Numeral to Integer. 


// 23. Write a JavaScript function to create a UUID identifier. 
// Note :
// According to Wikipedia - A universally unique identifier (UUID) is an identifier standard used in software construction. A UUID is simply a 128-bit value. The meaning of each bit is defined by any of several variants. For human-readable display, many systems use a canonical format using hexadecimal text with inserted hyphen characters. For example : de305d54-75b4-431b-adb2-eb6b9e546014



// 24. Write a JavaScript function to round a number to a specified number of digits and strip extra zeros (if any). 
// Test Data :
// var a = -4.55555;
// console.log(result);
// -4.5556
// var a = 5.0001000;
// console.log(result);
// 5.0001


// 25. Write a JavaScript function to make currency math (add, subtract, multiply, division etc.). 
// Test Data :
// n1 = '$40.24', n2 = '$21.57';


// 26. Write a JavaScript function to calculate the nth root of a number. 
// Test Data :
// console.log(nthroot(64, 2));
// 8
// console.log(nthroot(64, -2));
// 0.125


// 27. Write a JavaScript function to calculate degrees between 2 points with inverse Y axis. 
// Test Data :
// console.log(pointDirection(1, 0, 12, 0));
// 0
// console.log(pointDirection(1, 0, 1, 10));
// 90


// 28. Write a JavaScript function to round up an integer value to the next multiple of 5. 
// Test Data :
// console.log(int_round5(32));
// 35
// console.log(int_round5(137));
// 140


// 29. Write a JavaScript function to convert a positive number to negative number. 
// Test Data :
// console.log(pos_to_neg(15));
// -15


// 30. Write a JavaScript function to cast a square root of a number to an integer. 
// Test Data :
// console.log(sqrt_to_int(17));
// 4


// 31. Write a JavaScript function to get the highest number from three different numbers. 
// Test Data :
// console.log(highest_of_three(-5, 4, 2));
// 4


// 32. Write a JavaScript function to calculate the percentage (%) of a number. 
// Test Data :
// console.log(percentage(1000, 47.12));
// 471.2


// 33. Write a JavaScript function to convert degrees to radians. 
// Test Data :
// console.log(degrees_to_radians(45));
// 0.7853981633974483


// 34. Write a JavaScript function to convert radians to degrees. 
// Test Data :
// console.log(radians_to_degrees(0.7853981633974483));
// 45


// 35. Write a JavaScript function for the Pythagorean theorem. 
// According to Wikipedia : In mathematics, the Pythagorean theorem, also known as Pythagoras' theorem, is a relation in Euclidean geometry among the three sides of a right triangle. It states that the square of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the other two sides. The theorem can be written as an equation relating the lengths of the sides a, b and c, often called the "Pythagorean equation".
// Test Data :
// console.log(pythagorean(4, 3));
// 5


// 36. Write a JavaScript function which will return values that are powers of two. 
// Test Data :
// console.log(isPower_of_two(64));
// true
// console.log(isPower_of_two(94));
// false


// 37. Write a JavaScript function to limit a value inside a certain range. 
// Note : If the value is higher than max it will return max. and if the value is smaller than min it will return the min.
// Test Data :
// console.log(value_limit(7, 1, 12));
// 7
// console.log(value_limit(-7, 0, 12));
// 0
// console.log(value_limit(15, 0, 12));
// 12


// 38. Write a JavaScript function to check if a number is a whole number or has a decimal place. 
// Note : Whole Numbers are simply the numbers 0, 1, 2, 3, 4, 5, ... (and so on). No Fractions!
// Test Data :
// console.log(number_test(25.66));
// "Number has a decimal place."
// console.log(number_test(10));
// "It is a whole number."


// 39. Write a JavaScript function to print an integer with commas as thousands separators. 
// Test Data :
// console.log(thousands_separators(1000));
// "1,000"
// console.log(thousands_separators(10000.23));
// "10,000.23"
// console.log(thousands_separators(100000));
// "100,000"


// 40. Write a JavaScript function to create random background color. 


// 41. Write a JavaScript function to count the digits of an integer. 


// 42. Write a JavaScript function to calculate the combination of n and r. 
// The formula is : n!/(r!*(n - r)!).
// Test Data :
// console.log(combinations(6, 2));
// 15
// console.log(combinations(5, 3));
// 10


// 43. Write a JavaScript function to get all prime numbers from 0 to a specified number. 
// Test Data :
// console.log(primeFactorsTo(5));
// [2, 3, 5]
// console.log(primeFactorsTo(15));
// [2, 3, 5, 7, 11, 13]


// 44. Write a JavaScript function to show the first twenty Hamming numbers. 
// Hamming Numbers are numbers whose only prime factors are 2, 3 and 5.


// 45. Write a JavaScript function to subtract elements from one another in an array. 


// 46. Write a JavaScript function to calculate the divisor and modulus of two integers. 


// 47. Write a JavaScript function to calculate the extended Euclid Algorithm or extended GCD. 
// In mathematics, the Euclidean algorithm[a], or Euclid's algorithm, is an efficient method for computing the greatest common divisor (GCD) of two numbers, the largest number that divides both of them without leaving a remainder. It is named after the ancient Greek mathematician Euclid, who first described it in Euclid's Elements. It is an example of an algorithm, a step-by-step procedure for performing a calculation according to well-defined rules, and is one of the oldest algorithms in common use. It can be used to reduce fractions to their simplest form, and is a part of many other number-theoretic and cryptographic calculations.


// 48. Write a JavaScript function to calculate the falling factorial of a number. 
// Let x be a real number (but usually an integer).
// Let k be a positive integer.
// Then x to the (power of) k falling is :
// kth falling factorial power of x
// This is called the kth falling factorial power of x.


// 49. Write a JavaScript function to calculate Lanczos approximation gamma. 
// In mathematics, the Lanczos approximation is a method for computing the Gamma function numerically, published by Cornelius Lanczos in 1964. It is a practical alternative to the more popular Stirling's approximation for calculating the Gamma function with fixed precision.


// 50. Write a JavaScript program to add two complex numbers. 
// A complex number is a number that can be expressed in the form a + bi, where a and b are real numbers and i is the imaginary unit, that satisfies the equation i2 = −1. In this expression, a is the real part and b is the imaginary part of the complex number.


// 51. Write a JavaScript program to subtract two complex numbers. 


// 52. Write a JavaScript program to multiply two complex numbers. 


// 53. Write a JavaScript program to divide two complex numbers. 




Object.html // 1. Write a JavaScript program to list the properties of a JavaScript object.
// Sample object:
// var student = {
// name : "David Rayy",
// sclass : "VI",
// rollno : 12 };
// Sample Output: name,sclass,rollno


// 2. Write a JavaScript program to delete the rollno property from the following object. Also print the object before or after deleting the property.
// Sample object:
// var student = {
// name : "David Rayy",
// sclass : "VI",
// rollno : 12 };


// 3. Write a JavaScript program to get the length of a JavaScript object.
// Sample object :
// var student = {
// name : "David Rayy",
// sclass : "VI",
// rollno : 12 };


// 4. Write a JavaScript program to display the reading status (i.e. display book name, author name and reading status) of the following books.

// var library = [ 
//    {
//        author: 'Bill Gates',
//        title: 'The Road Ahead',
//        readingStatus: true
//    },
//    {
//        author: 'Steve Jobs',
//        title: 'Walter Isaacson',
//        readingStatus: true
//    },
//    {
//        author: 'Suzanne Collins',
//        title:  'Mockingjay: The Final Book of The Hunger Games', 
//        readingStatus: false
//    }];



// 5. Write a JavaScript program to get the volume of a Cylinder with four decimal places using object classes.
// Volume of a cylinder : V = πr2h
// where r is the radius and h is the height of the cylinder.


// 6. Write a Bubble Sort algorithm in JavaScript.
// Note : Bubble sort is a simple sorting algorithm that works by repeatedly stepping through the list to be sorted,
// Sample Data: [6,4,0, 3,-2,1]
// Expected Output : [-2, 0, 1, 3, 4, 6]


// 7. Write a JavaScript program which returns a subset of a string.
// Sample Data: dog
// Expected Output: ["d", "do", "dog", "o", "og", "g"]


// 8. Write a JavaScript program to create a Clock.
// Note: The output will come every second.
// Expected Console Output :
// "14:37:42"
// "14:37:43"
// "14:37:44"
// "14:37:45"
// "14:37:46"
// "14:37:47"


// 9. Write a JavaScript program to calculate the area and perimeter of a circle.
// Note : Create two methods to calculate the area and perimeter. The radius of the circle will be supplied by the user.


// 10. Write a JavaScript program to sort an array of JavaScript objects.
// Sample Object :

// var library = [ 
//    {
//        title:  'The Road Ahead',
//        author: 'Bill Gates',
//        libraryID: 1254
//    },
//    {
//        title: 'Walter Isaacson',
//        author: 'Steve Jobs',
//        libraryID: 4264
//    },
//    {
//        title: 'Mockingjay: The Final Book of The Hunger Games',
//        author: 'Suzanne Collins',
//        libraryID: 3245
//    }];

// Expected Output:

// [[object Object] {
//   author: "Walter Isaacson",
//   libraryID: 4264,
//   title: "Steve Jobs"
// }, [object Object] {
//   author: "Suzanne Collins",
//   libraryID: 3245,
//   title: "Mockingjay: The Final Book of The Hunger Games"
// }, [object Object] {
//   author: "The Road Ahead",
//   libraryID: 1254,
//   title: "Bill Gates"
// }]



// 11. Write a JavaScript function to print all the methods in an JavaScript object.
// Test Data :
// console.log(all_properties(Array));
// ["length", "name", "arguments", "caller", "prototype", "isArray", "observe", "unobserve"]


// 12. Write a JavaScript function to parse an URL.


// 13. Write a JavaScript function to retrieve all the names of object's own and inherited properties.


// 14. Write a JavaScript function to retrieve all the values of an object's properties.


// 15. Write a JavaScript function to convert an object into a list of `[key, value]` pairs.


// 16. Write a JavaScript function to get a copy of the object where the keys have become the values and the values the keys.


// 17. Write a JavaScript function to check whether an object contains given property.


// 18. Write a JavaScript function to check whether a given value is a DOM element.




Recursion.html // 1. Write a JavaScript program to calculate the factorial of a number. 
// In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example, 5! = 5 x 4 x 3 x 2 x 1 = 120
// Click me to see the solution

// 2. Write a JavaScript program to find the greatest common divisor (gcd) of two positive numbers. 


// 3. Write a JavaScript program to get the integers in range (x, y). 
// Example : range(2, 9)
// Expected Output : [3, 4, 5, 6, 7, 8]


// 4. Write a JavaScript program to compute the sum of an array of integers. 
// Example : var array = [1, 2, 3, 4, 5, 6]
// Expected Output : 21


// 5. Write a JavaScript program to compute the exponent of a number. 
// Note : The exponent of a number says how many times the base number is used as a factor.
// 82 = 8 x 8 = 64. Here 8 is the base and 2 is the exponent.


// 6. Write a JavaScript program to get the first n Fibonacci numbers. 
// Note : The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, . . . Each subsequent number is the sum of the previous two.


// 7. Write a JavaScript program to check whether a number is even or not. 


// 8. Write a JavaScript program for binary search. 
// Sample array : [0,1,2,3,4,5,6]
// console.log(l.br_search(5)) will return '5'


// 9. Write a merge sort program in JavaScript. 
// Sample array : [34,7,23,32,5,62]
// Sample output : [5, 7, 23, 32, 34, 62]




String.html // 1. Write a JavaScript function to check whether an `input` is a string or not. 
// Test Data :
// console.log(is_string('w3resource'));
// true
// console.log(is_string([1, 2, 4, 0]));
// false
// Click me to see the solution

// 2. Write a JavaScript function to check whether a string is blank or not. 
// Test Data :
// console.log(is_Blank(''));
// console.log(is_Blank('abc'));
// true
// false
// Click me to see the solution

// 3. Write a JavaScript function to split a string and convert it into an array of words. 
// Test Data :
// console.log(string_to_array("Robin Singh"));
// ["Robin", "Singh"]
// Click me to see the solution

// 4. Write a JavaScript function to extract a specified number of characters from a string. 
// Test Data :
// console.log(truncate_string("Robin Singh",4));
// "Robi"


// 5. Write a JavaScript function to convert a string in abbreviated form. 
// Test Data :
// console.log(abbrev_name("Robin Singh"));
// "Robin S."


// 6. Write a JavaScript function to hide email addresses to protect from unauthorized user. 
// Test Data :
// console.log(protect_email("robin_singh@example.com"));
// "robin...@example.com"


// 7. Write a JavaScript function to parameterize a string. 
// Test Data :
// console.log(string_parameterize("Robin Singh from USA."));
// "robin-singh-from-usa"


// 8. Write a JavaScript function to capitalize the first letter of a string. 
// Test Data :
// console.log(capitalize('js string exercises'));
// "Js string exercises"


// 9. Write a JavaScript function to capitalize the first letter of each word in a string. 
// Test Data :
// console.log(capitalize_Words('js string exercises'));
// "Js String Exercises"


// 10. Write a JavaScript function that takes a string which has lower and upper case letters as a parameter and converts upper case letters to lower case, and lower case letters to upper case. 
// Test Data :
// console.log(swapcase('AaBbc'));
// "aAbBC"


// 11. Write a JavaScript function to convert a string into camel case.
// Test Data :
// console.log(camelize("JavaScript Exercises"));
// console.log(camelize("JavaScript exercises"));
// console.log(camelize("JavaScriptExercises"));
// "JavaScriptExercises"
// "JavaScriptExercises"
// "JavaScriptExercises"


// 12. Write a JavaScript function to uncamelize a string. 
// Test Data :
// console.log(uncamelize('helloWorld'));
// console.log(uncamelize('helloWorld','-'));
// console.log(uncamelize('helloWorld','_'));
// "hello world"
// "hello-world"
// "hello_world"


// 13. Write a JavaScript function to concatenates a given string n times (default is 1). 
// Test Data :
// console.log(repeat('Ha!'));
// console.log(repeat('Ha!',2));
// console.log(repeat('Ha!',3));
// "Ha!"
// "Ha!Ha!"
// "Ha!Ha!Ha!"


// 14. Write a JavaScript function to insert a string within a string at a particular position (default is 1).
// Test Data :
// console.log(insert('We are doing some exercises.'));
// console.log(insert('We are doing some exercises.','JavaScript '));
// console.log(insert('We are doing some exercises.','JavaScript ',18));
// "We are doing some exercises."
// "JavaScript We are doing some exercises."
// "We are doing some JavaScript exercises."


// 15. Write a JavaScript function to humanized number (Formats a number to a human-readable string.) with the correct suffix such as 1st, 2nd, 3rd or 4th. 
// Test Data :
// console.log(humanize_format());
// console.log(humanize_format(1));
// console.log(humanize_format(8));
// console.log(humanize_format(301));
// console.log(humanize_format(402));
// "1st"
// "8th"
// "301st"
// "402nd"


// 16. Write a JavaScript function to truncates a string if it is longer than the specified number of characters. Truncated strings will end with a translatable ellipsis sequence ("…") (by default) or specified characters. 
// Test Data :
// console.log(text_truncate('We are doing JS string exercises.'))
// console.log(text_truncate('We are doing JS string exercises.',19))
// console.log(text_truncate('We are doing JS string exercises.',15,'!!'))
// "We are doing JS string exercises."
// "We are doing JS ..."
// "We are doing !!"


// 17. Write a JavaScript function to chop a string into chunks of a given length. 
// Test Data :
// console.log(string_chop('w3resource'));
// console.log(string_chop('w3resource',2));
// console.log(string_chop('w3resource',3));
// ["w3resource"]
// ["w3", "re", "so", "ur", "ce"]
// ["w3r", "eso", "urc", "e"]


// 18. Write a JavaScript function to count the occurrence of a substring in a string. 
// Test Data :
// console.log(count("The quick brown fox jumps over the lazy dog", 'the'));
// Output :
// 2
// console.log(count("The quick brown fox jumps over the lazy dog", 'fox',false));
// Output :
// 1


// 19. Write a JavaScript function to escape a HTML string. 
// Test Data :
// console.log(escape_HTML('<a href="javascript-string-exercise-17.php" target="_blank">'));
// Output :
// "&lt;a href=&quot;javascript-string-exercise-17.php&quot; target=&quot;_blank&quot;&gt;"


// 20. Write a JavaScript function that can pad (left, right) a string to get to a determined length. 
// Test Data :
// console.log(formatted_string('0000',123,'l'));
// console.log(formatted_string('00000000',123,''));
// Output :
// "0123"
// "12300000"


// 21. Write a JavaScript function to repeat a string a specified times. 
// Test Data :
// console.log(repeat_string('a', 4));
// console.log(repeat_string('a'));
// Output :
// "aaaa"
// "Error in string or count."


// 22. Write a JavaScript function to get a part of a string after a specified character.
// Test Data :
// console.log(subStrAfterChars('w3resource: JavaScript Exercises', ':','a'));
// console.log(subStrAfterChars('w3resource: JavaScript Exercises', 'E','b'));
// Output :
// "w3resource"
// "xercises"


// 23. Write a JavaScript function to strip leading and trailing spaces from a string. 
// Test Data :
// console.log(strip('w3resource '));
// console.log(strip(' w3resource'));
// console.log(strip(' w3resource '));
// Output :
// "w3resource"
// "w3resource"
// "w3resource"


// 24. Write a JavaScript function to truncate a string to a certain number of words. 
// Test Data :
// console.log(truncate('The quick brown fox jumps over the lazy dog', 4));
// Output :
// "The quick brown fox"


// 25. Write a JavaScript function to alphabetize a given string. 
// Alphabetize string : An individual string can be alphabetized. This rearranges the letters so they are sorted A to Z.
// Test Data :
// console.log(alphabetize_string('United States'));
// Output :
// "SUadeeinsttt"


// 26. Write a JavaScript function to remove the first occurrence of a given 'search string' from a string. 
// Test Data :
// console.log(remove_first_occurrence("The quick brown fox jumps over the lazy dog", 'the'));
// Output :
// "The quick brown fox jumps over lazy dog"


// 27. Write a JavaScript function to convert ASCII to Hexadecimal format. 
// Test Data :
// console.log(ascii_to_hexa('12'));
// console.log(ascii_to_hexa('100'));
// Output :
// "3132"
// "313030"


// 28. Write a JavaScript function to convert Hexadecimal to ASCII format. 
// Test Data :
// console.log(hex_to_ascii('3132'));
// console.log(hex_to_ascii('313030'));
// Output :
// "12"
// "100"


// 29. Write a JavaScript function to find a word within a string. 
// Test Data :
// console.log(search_word('The quick brown fox', 'fox'));
// console.log(search_word('aa, bb, cc, dd, aa', 'aa'));
// Output :
// "'fox' was found 1 times."
// "'aa' was found 2 times."


// 30. Write a JavaScript function check if a string ends with specified suffix. 
// Test Data :
// console.log(string_endsWith('JS PHP PYTHON','PYTHON'));
// true
// console.log(string_endsWith('JS PHP PYTHON',''));
// false


// 31. Write a JavaScript function to escapes special characters (&, <, >, ', ") for use in HTML. 
// Test Data :
// console.log(escape_html('PHP & MySQL'));
// "PHP &amp; MySQL"
// console.log(escape_html('3 > 2'));
// "3 &gt; 2"


// 32. Write a JavaScript function to remove?non-printable ASCII chars. 
// Test Data :
// console.log(remove_non_ascii('???????PHP-MySQL??????'));
// "PHP-MySQL"


// 33. Write a JavaScript function to remove non-word characters. 
// Test Data :
// console.log(remove_non_word('PHP ~!@#$%^&*()+`-={}[]|\\:";\'/?><., MySQL'));
// "PHP - MySQL"


// 34. Write a JavaScript function to convert a string to title case. 
// Test Data :
// console.log(sentenceCase('PHP exercises. python exercises.'));
// "Php Exercises. Python Exercises."


// 35. Write a JavaScript function to remove HTML/XML tags from string. 
// Test Data :
// console.log(strip_html_tags('<p><strong><em>PHP Exercises</em></strong></p>'));
// "PHP Exercises"


// 36. Write a JavaScript function to create a Zerofilled value with optional +, - sign. 
// Test Data :
// console.log(zeroFill(120, 5, '-'));
// "+00120"
// console.log(zeroFill(29, 4));
// "0029"


// 37. Write a JavaScript function to test case insensitive (except special Unicode characters) string comparison. 
// Test Data :
// console.log(compare_strings('abcd', 'AbcD'));
// true
// console.log(compare_strings('ABCD', 'Abce'));
// false


// 38. Write a JavaScript function to create a case-insensitive search. 
// Test Data :
// console.log(case_insensitive_search('JavaScript Exercises', 'exercises'));
// "Matched"
// console.log(case_insensitive_search('JavaScript Exercises', 'Exercises'));
// "Matched"
// console.log(case_insensitive_search('JavaScript Exercises', 'Exercisess'));
// "Not Matched"


// 39. Write a JavaScript function to Uncapitalize? the first character of a string. 
// Test Data :
// console.log(Uncapitalize('Js string exercises'));
// "js string exercises"


// 40. Write a JavaScript function to Uncapitalize the first letter of each word of a string. 
// Test Data :
// console.log(unCapitalize_Words('Js String Exercises'));
// "js string exercises"


// 41. Write a JavaScript function to capitalize each word in the string. 
// Test Data :
// console.log(capitalizeWords('js string exercises'));
// "JS STRING EXERCISES"


// 42. Write a JavaScript function to uncapitalize each word in the string. 
// Test Data :
// console.log(unCapitalizeWords('JS STRING EXERCISES'));
// "js string exercises"


// 43. Write a JavaScript function to test whether the character at the provided (character) index is upper case. 
// Test Data :
// console.log(isUpperCaseAt('Js STRING EXERCISES', 1));
// false


// 44. Write a JavaScript function to test whether the character at the provided (character) index is lower case. 
// Test Data :
// console.log(isLowerCaseAt ('Js STRING EXERCISES', 1));
// true


// 45. Write a JavaScript function to get humanized number with the correct suffix such as 1st, 2nd, 3rd or 4th. 
// Test Data :
// console.log(humanize(1));
// console.log(humanize(20));
// console.log(humanize(302));
// "1st"
// "20th"
// "302nd"


// 46. Write a JavaScript function to test whether a string starts with a specified string. 
// Test Data :
// console.log(startsWith('js string exercises', 'js'));
// true


// 47. Write a JavaScript function to test whether a string ends with a specified string. 
// Test Data :
// console.log(endsWith('JS string exercises', 'exercises'));
// true


// 48. Write a JavaScript function to get the successor of a string. 

// Note: The successor is calculated by incrementing characters starting from the rightmost alphanumeric (or the rightmost character if there are no alphanumerics) in the string. Incrementing a digit always results in another digit, and incrementing a letter results in another letter of the same case. If the increment generates a carry, the character to the left of it is incremented. This process repeats until there is no carry, adding an additional character if necessary.
// Example :
// string.successor("abcd") == "abce"
// string.successor("THX1138") == "THX1139"
// string.successor("< >") == "< >"
// string.successor("1999zzz") == "2000aaa"
// string.successor("ZZZ9999") == "AAAA0000"

// Test Data :
// console.log(successor('abcd'));
// console.log(successor('3456'));
// "abce"
// "3457"


// 49. Write a JavaScript function to get unique guid (an acronym for 'Globally Unique Identifier?) of the specified length, or 32 by default. 
// Test Data :
// console.log(guid());
// console.log(guid(15));
// "hRYilcoV7ajokxsYFl1dba41AyE0rUQR"
// "b7pwBqrZwqaDrex"




Validation and Regular Expression.html // 1. Write a JavaScript program to test the first character of a string is uppercase or not.


// 2. Write a JavaScript program to check a credit card number.


// 3. Write a pattern that matches e-mail addresses.
// The personal information part contains the following ASCII characters.

//     Uppercase (A-Z) and lowercase (a-z) English letters.
//     Digits (0-9).
//     Characters ! # $ % & ' * + - / = ? ^ _ ` { | } ~
//     Character . ( period, dot or fullstop) provided that it is not the first or last character and it will not come one after the other.



// 4. Write a JavaScript program to search a date within a string.



// 5. Write a JavaScript program that work as a trim function (string) using regular expression.



// 6. Write a JavaScript program to count number of words in string.
// Note :
// - Remove white-space from start and end position.
// - Convert 2 or more spaces to 1.
// - Exclude newline with a start spacing.



// 7. Write a JavaScript function to check whether a given value is IP value or not.



// 8. Write a JavaScript function to count the number of vowels in a given string.
// Test Data :
// console.log(alphabetize_string('United States'));
// Output :
// "SUadeeinsttt"



// 9. Write a JavaScript function to check whether a given value is an valid url or not.



// 10. Write a JavaScript function to check whether a given value is alpha numeric or not.



// 11. Write a JavaScript function to check whether a given value is time string or not.



// 12. Write a JavaScript function to check whether a given value is US zip code or not.



// 13. Write a JavaScript function to check whether a given value is UK Post Code or not.



// 14. Write a JavaScript function to check whether a given value is Canada Post Code or not.



// 15. Write a JavaScript function to check whether a given value is a social security number or not.



// 16. Write a JavaScript function to check whether a given value is hexadecimal value or not.



// 17. Write a JavaScript function to check whether a given value is hexcolor value or not.



// 18. Write a JavaScript function to check whether a given value represents a domain or not.



// 19. Write a JavaScript function to check whether a given value is html or not.Go to the editor



// 20. Write a JavaScript function to check a given value contains alpha, dash and underscore.



// 21. Write a JavaScript function to print an integer with commas as thousands separators.

// Test Data :
// console.log(thousands_separators(1000));
// "1,000"
// console.log(thousands_separators(10000.23));
// "10,000.23"
// console.log(thousands_separators(100000));
// "100,000"

