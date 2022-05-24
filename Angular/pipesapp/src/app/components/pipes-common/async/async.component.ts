import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-async',
  templateUrl: './async.component.html',
  styleUrls: ['./async.component.css']
})
export class AsyncComponent implements OnInit {

  img = new Promise((resolve, reject) => {
    resolve("https://javadesde0.com/wp-content/uploads/87018c00-694b-11e9-8b5f-c34826306d36-768x384.png")
  });

  constructor() { }

  ngOnInit(): void {
  }

}
