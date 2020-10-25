import { Component, OnInit } from '@angular/core';
import data from '../../../data/data.json';


@Component({
  selector: 'app-cavexml-search',
  templateUrl: './cavexml-search.component.html',
  styleUrls: ['./cavexml-search.component.scss']
})
export class CavexmlSearchComponent implements OnInit {
  public tag; 
  public length;
  public vertical_extent;
  public altitude;
  public length_gtlt;
  public vertical_extent_gtlt;
  public altitude_gtlt;

  // when Submit button is pressed
  onClickMe() {
    window.alert(
      "tag: " + this.tag +
      "\nlength: " + this.length +
      "\nvertical_extent: " + this.vertical_extent +
      "\naltitude: " + this.altitude +
      "\nlength_gtlt: " + this.length_gtlt +
      "\nvertical_extent_gtlt: " + this.vertical_extent_gtlt +
      "\naltitude_gtlt: " + this.altitude_gtlt
    );
  }

  // when length value is entered
  OnInputLen(value) {
    this.length = value;
  }

  // when vertical_extent value is entered
  OnInputVE(value) {
    this.vertical_extent = value;
  }

  // when altitude value is entered
  OnInputAlt(value) {
    this.altitude = value;
  }

  // This is dummy data
  public dummyData = [
    {
      name: 'Test Cave 1',
      tags: 'Cave, SSSI',
      length: 112,
      vr: 22,
      altitude: 123
    },
    {
      name: 'Test Cave 2',
      tags: 'Cave, SSSI',
      length: 112,
      vr: 22,
      altitude: 123
    },
    {
      name: 'Test Cave 3',
      tags: 'Cave, SSSI',
      length: 112,
      vr: 22,
      altitude: 123
    },
  ];

  constructor() {
    this.dummyData = data
    // console.log('Reading local json files');
    // console.log(data);
  }

  ngOnInit() {
  }
  p: number = 1;

}
