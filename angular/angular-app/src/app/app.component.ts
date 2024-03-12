import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { AppService } from './app.service';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  
  configuration: any;
  presetsArray: any;
  optionsArray: any;

  title = 'angular-app';

  constructor(private appService: AppService) {}

  ngOnInit(): void {
    console.log("Going into ngOnInit now");
    this.appService.getData().subscribe(data => {
      console.log(data);
      this.configuration = data.configuration;
      this.presetsArray = data.presetsArray;
      this.optionsArray = data.optionsArray;
    });
  }

}
