use std::env;
use std::io;
use std::io::prelude::*;
use std::io::BufReader;
use std::fs::File;



fn main() {
    let path = env::current_dir().unwrap();
    println!("{}", path.display());

    //This is approach is outlined in the documentation for std::io under 'Iterator types'.
    let poem = File::open("The Raven.txt")?;
    let reader = BufReader::new(poem);
    let mut count = 0;
    for i in reader.lines() {
        if count < 10 {
            println!("{}", i?);
            count += 1;
        } else {
            break
        }
    }
}