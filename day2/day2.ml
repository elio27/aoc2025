let read_file filename =
  let ch = open_in filename in
  let s = really_input_string ch (in_channel_length ch) in
  close_in ch;
  s
;;

let rec rep str s n =
  if n <= 0 then ""
  else s ^ (rep str s (n - 1))

let rec process_ranges ranges s_half s= 
  match ranges with
  | [] -> (s_half, s)
  | h :: t -> 
    let sp = String.split_on_char '-' h in
    let (a, b) = match sp with
      | [x; y] -> (int_of_string x, int_of_string y)
      | _ -> failwith "Invalid range format"
    in

    let rec loop_ids id acc_s_half acc_s = 
      if id > b then (acc_s_half, acc_s)
      else
        let s_id = string_of_int id in
        let l = String.length s_id in
        if s_id = rep "" (String.sub s_id 0 (l/2)) 2 then
          loop_ids (id+1) (acc_s_half + id) (acc_s + id)
        else

          let rec check_subs k = 
            if k > l / 2 then false
            else if l mod k = 0 then
              let pat = String.sub s_id 0 k in
              if s_id = rep "" pat (l/k) then true
              else check_subs (k+1)
            else check_subs (k+1)
          in
          if check_subs 1 then
            loop_ids (id+1) acc_s_half (acc_s + id)
          else
            loop_ids (id+1) acc_s_half acc_s
      in
      let (new_s_half, new_s) = loop_ids a s_half s in
      process_ranges t new_s_half new_s

;;

let solve filename =
  let inp = read_file filename in
  let ranges = String.split_on_char ',' inp in
  process_ranges ranges 0 0
;;

let file = "./input.txt"
let (sum_half, sum_total) = solve file
let () =
  Printf.printf "Sum of invalid IDs according to the 'repeating twice' rule: %d\n" sum_half;
  Printf.printf "Sum of invalid IDs according to the 'any repeating sequence' rule: %d\n" sum_total