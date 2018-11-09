import { Component, OnInit } from '@angular/core';

import { MAJOR_ROLE_TOOL_LIST, s3MediaResource } from "../services/media.mock-data";
import { MediaContentService } from "../services/media-content.service";

@Component({
    selector: 'app-major-roles',
    templateUrl: './major-roles.component.html',
    styleUrls: ['./major-roles.component.scss']
})
export class MajorRolesComponent implements OnInit {

    public tools: s3MediaResource[];
    public educations: any;

    constructor(
        private mediaService: MediaContentService,
    ) { }

    ngOnInit() {
        
        // load in data
        this.tools = this.mediaService.majorRolesToolList;
        this.educations = this.mediaService.majorRolesEducations;
    }

}
