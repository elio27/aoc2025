let read_file filename =
  let ch = open_in filename in
  let s = really_input_string ch (in_channel_length ch) in
  close_in ch;
  s

let solve filename =
  let inp = read_file filename in
  let instructions = String.split_on_char '\n' inp in

  let rec process_instr instructions dial zeros clicks =
    match instructions with
    | [] -> (zeros, clicks)
    | instr::t -> 
        let turn = instr.[0] in
        let dist = int_of_string (String.sub instr 1 (String.length instr - 1)) in

        (* Mod distance and add clicks *)
        let click_mod = clicks + dist / 100 in
        let dist = dist mod 100 in

        (* Add dist, and maybe another click *)
        let (new_dial, new_click) =
          if turn = 'L' then
            let new_click = if dist >= dial && dial <> 0 then 1 else 0 in
            (dial - dist, new_click)
          else
            let new_click = if dist >= 100 - dial && dial <> 0 then 1 else 0 in
            (dial + dist, new_click)
          in
        
        (* Mod dial and maybe add a zero *)
        let new_dial = if new_dial < 0 then new_dial + 100 else new_dial mod 100 in
        let new_zeros = if dial = 0 then zeros + 1 else zeros in

        (* Recursive call *)
        process_instr t new_dial new_zeros (click_mod + new_click)
        in

  process_instr instructions 50 0 0

(* Run *)
let file = "./input.txt"
let (zeros, clicks) = solve file
let () =
  Printf.printf "Zeros: %d\n" zeros;
  Printf.printf "Clicks: %d\n" clicks