import { Component, OnInit } from '@angular/core';
import { Team } from '../team';
import { TEAMS } from '../mock-teams';
import { ApiDataService } from '../apiData/api.data.service';

@Component({
  selector: 'app-team-list',
  templateUrl: './team-list.component.html',
  styleUrls: ['./team-list.component.scss']
})
export class TeamListComponent implements OnInit {

  teams: Team[] = new Array<Team>();
  selectedTeam?: Team;
  displayedColumns  :  string[] = ['id', 'fullName', 'name', 'abbreviation', 'city', 'conference', 'division'];
  
  constructor(private apiDataService: ApiDataService) { 
    //console.info('In constructor')
  }

  ngOnInit(): void {
    // this is api data:
    this.apiDataService.getTeamList()
    .subscribe((data) => {    
    this.teams = data
    });
  }

  onSelect(team: Team): void {
    this.selectedTeam = team;
  }

}
