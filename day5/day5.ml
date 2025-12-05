
let read_file filename =
  let ch = open_in filename in
  let s = really_input_string ch (in_channel_length ch) in
  close_in ch;
  s
;;


let parse input =
  let lines = String.split_on_char '\n' input in
  let rec aux acc current = function
    | [] -> List.rev (current :: acc)
    | "" :: rest -> aux (current :: acc) [] rest
    | line :: rest -> aux acc (line :: current) rest
  in
  match aux [] [] lines with
  | [p1; p2] -> p1, p2
  | _ -> failwith "Whatever..."
;;

let p1, p2 = read_file "input.txt" |> parse

let ranges = List.map (fun s -> 
                      match String.split_on_char '-' s with
                      | [a; b]-> (int_of_string a, int_of_string b)
                      | _ -> failwith "Man I hate these warnings") p1
let ids = List.map int_of_string p2

(* Part 1 *)
let rec loop_ids ids acc =
  let rec loop_ranges ranges id acc =
    match ranges with
    | [] -> acc
    | (a, b)::t -> if a <= id  && id <= b then acc + 1 else loop_ranges t id acc
  in
  match ids with
  | [] -> acc
  | id::t -> loop_ids t (loop_ranges ranges id acc)
;;

let fresh_count_1 = loop_ids ids 0

(* Part 2 *)
let merge ranges =
  let rec aux ranges merged =
    match ranges with
    | [] -> List.rev merged
    | (a, b)::t -> match merged with
                  | [] -> aux t [(a, b)]
                  | (a', b')::t' -> if a <= b' + 1 then aux t ((a', max b b')::t')
                                    else aux t ((a, b)::merged)
  in
  aux ranges []
;;

let sum_count ranges =
  let rec aux ranges acc = 
    match ranges with
    | [] -> acc
    | (a, b)::t -> aux t (acc + b - a + 1)
  in
  aux ranges 0
;;

let fresh_count_2 = ranges |> List.sort compare
                           |> merge
                           |> sum_count


let () = 
  Printf.printf "Part 1: %d\n" (fresh_count_1);
  Printf.printf "Part 2: %d\n" (fresh_count_2)