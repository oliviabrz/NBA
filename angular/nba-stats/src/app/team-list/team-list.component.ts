import { Component, OnInit, AfterViewInit, ViewChild } from '@angular/core';
import { Team } from '../team';
import { TEAMS } from '../mock-teams';
import { ApiDataService } from '../apiData/api.data.service';
import { MatTableDataSource } from '@angular/material/table';
import { Kvp } from '../kvp';
import { MatPaginator } from '@angular/material/paginator';

@Component({
  selector: 'app-team-list',
  templateUrl: './team-list.component.html',
  styleUrls: ['./team-list.component.scss']
})
export class TeamListComponent implements OnInit, AfterViewInit {

  @ViewChild(MatPaginator) paginator!: MatPaginator;
  teams: Team[] = new Array<Team>();
  dsTable: MatTableDataSource<Team>;
  selectedTeam?: Team;
  displayedColumns  :  string[] = ['id', 'fullName', 'name', 'abbreviation', 'city', 'conference', 'division'];
  
  constructor(private apiDataService: ApiDataService) { 
    this.dsTable = new MatTableDataSource<Team>();
    //console.info('In constructor')
  }

  ngOnInit(): void {
    // this is api data:
    this.apiDataService.getTeamList()
    .subscribe((data) => {    
    this.dsTable.data = data
    });
    
  }
  ngAfterViewInit() {
    this.dsTable.paginator = this.paginator;
  }
  onSelect(team: Team): void {
    this.selectedTeam = team;
  }

}
