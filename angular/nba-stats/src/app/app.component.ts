import { Component, OnInit } from '@angular/core';
import { AppStateService } from './app-state';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'NBA Player Stats';
  loadPlayersComponent: boolean = false;
  loadTeamsComponent: boolean = false;
  loadGamesComponent: boolean = false;
  loadGameStatsComponent: boolean = false;

  constructor(public appState: AppStateService) {
    console.info('In app-component constructor')
  }

  ngOnInit(): void {
  
  }
    LoadComponent(componentName:string){
      console.log(componentName)
      if (componentName == 'Players') {
       this.loadPlayersComponent = true;
       this.loadTeamsComponent = false;
       this.loadGamesComponent = false;
       this.loadGameStatsComponent = false;
      }
      else if (componentName == 'Teams') {
        this.loadPlayersComponent = false;
        this.loadTeamsComponent = true;
        this.loadGamesComponent = false;
        this.loadGameStatsComponent = false;
       }
       else if (componentName == 'Games') {
        this.loadPlayersComponent = false;
        this.loadTeamsComponent = false;
        this.loadGamesComponent = true;
        this.loadGameStatsComponent = false;
       }
       else if (componentName == 'GameStats') {
        this.loadPlayersComponent = false;
        this.loadTeamsComponent = false;
        this.loadGamesComponent = false;
        this.loadGameStatsComponent = true;
       }
  }   
}
