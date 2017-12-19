use std::env;
use std::io;
use std::io::prelude::*;
use std::io::BufReader;
use std::fs::File;



fn main() {
    let path = env::current_dir().unwrap();
    println!("{}", path.display());
}

