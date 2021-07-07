import { Component, OnInit } from '@angular/core';
import { Team } from '../team';
import { TEAM } from '../mock-team';
import { ApiDataService } from '../apiData/api.data.service';

@Component({
  selector: 'app-team',
  templateUrl: './team.component.html',
  styleUrls: ['./team.component.scss']
})
export class TeamComponent implements OnInit {

  teams: Team[] = TEAM;
  tableData: any[] | undefined;

  //selectedTeam?: Team;
  //displayedColumns  :  string[] = ['abbreviation', ' city', 'conference', 'division', 'fullName', 'id', 'name'] 
  
  constructor(private apiDataService: ApiDataService) { }

  ngOnInit(): void {
    let dictList: [{ [name: string]: any }] = [{}];
    for (let team of this.teams) {      
        let kvp: { [name: string]: any } = {}
        kvp.Abbreviation = team.Abbreviation
        dictList.push(kvp)

        kvp = {}
        kvp.City = team.City
        dictList.push(kvp)
    }
    this.tableData = dictList;
    // .subscribe((data) => {    
    //   this.teams = data
    // });
  }

  // onSelect(team: Team): void {
  //   this.selectedTeam = team;
  // }

}


