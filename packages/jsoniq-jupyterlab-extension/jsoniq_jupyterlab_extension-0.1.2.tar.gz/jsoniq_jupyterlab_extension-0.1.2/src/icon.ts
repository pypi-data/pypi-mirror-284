export const NS = 'davidbuzatu-marian/jsoniq-jupyter-plugin';

import { LabIcon } from '@jupyterlab/ui-components';

import jsoniqSVG from '../images/JSONiq.svg';

export const jsoniqIcon = new LabIcon({
  svgstr: jsoniqSVG,
  name: `${NS}:jsoniq`
});
