import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-cavexml-search',
  templateUrl: './cavexml-search.component.html',
  styleUrls: ['./cavexml-search.component.scss']
})
export class CavexmlSearchComponent implements OnInit {

  // This is dummy data
  public dummyData = [
    {
      name: 'Test Cave',
      tags: 'Cave, SSSI',
      length: 112,
      vr: 22,
      altitude: 123
    },
    {
      name: 'Test Cave',
      tags: 'Cave, SSSI',
      length: 112,
      vr: 22,
      altitude: 123
    },
    {
      name: 'Test Cave',
      tags: 'Cave, SSSI',
      length: 112,
      vr: 22,
      altitude: 123
    },
];
  constructor() { }

  ngOnInit() {
  }
  p: number = 1;

}
