import { Component, OnInit } from '@angular/core';
import { AppStateService } from './app-state';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'NBA Player Stats';

  constructor(public appState: AppStateService) {
    console.info('In app-component constructor')
  }

  ngOnInit(): void {
  
  }
}
