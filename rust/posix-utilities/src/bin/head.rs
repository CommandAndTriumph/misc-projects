use std::env;
use std::io;
use std::io::prelude::*;
use std::io::BufReader;
use std::fs::File;



fn main() {
    //This is approach is outlined in the documentation for std::io under 'Iterator types'.
    let file_name = env::args().nth(1).unwrap();
    let fh = match File::open(&file_name){
        Err(_) => panic!("File name is incorrect."),
        Ok(t) => t,
    };
    let reader = BufReader::new(fh);
    let mut count = 0;
    for i in reader.lines() {
        if count < 10 {
            if let Ok(line) = i {
                println!("{}", line);
                count += 1;
            } else {
                panic!("A line has failed to read.  File: {}, Error: {}", file_name, i.unwrap_err())
            }
        }
    }
}