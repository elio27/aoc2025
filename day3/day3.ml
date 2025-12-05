let read_file filename =
  let ch = open_in filename in
  let s = really_input_string ch (in_channel_length ch) in
  close_in ch;
  s
;;

let rec find_max lst =
  match lst with
  | [] -> 0
  | [x] -> x
  | h::t -> max h (find_max t)
;;

let find_index predicate lst =
  let rec aux lst index =
    match lst with
    | [] -> -1
    | h::t -> if predicate h then index else aux t (index + 1)
  in aux lst 0
;;


let total_joltage lines n =
  let rec aux lines current_total = 
    match lines with
    | [] -> current_total
    | line::t ->
      let int_line = List.map int_of_char (List.init (String.length line) (String.get line)) in
      
      let rec loop_digits i curr_str curr_index = 
        if i >= n then curr_str
        else
          let interesting_digits = List.filteri (fun j _ -> j >= curr_index && j < List.length int_line - (n - i - 1)) int_line in
          let d = find_max interesting_digits in
          let curr_index = curr_index + (find_index (fun x -> x = d) interesting_digits) + 1 in
          loop_digits (i + 1) (curr_str ^ (String.make 1 (char_of_int d))) curr_index
      in
      let new_total = current_total + int_of_string (loop_digits 0 "" 0) in
      aux t new_total
  in
  aux lines 0
;;

let lines = 
  read_file "./input.txt" |> String.split_on_char '\n'
let total_2_digits = total_joltage lines 2
let total_12_digits = total_joltage lines 12

let () =
  Printf.printf "Total Output Joltage for 2 digits: %d\n" total_2_digits;
  Printf.printf "Total Output Joltage for 12 digits: %d\n" total_12_digits