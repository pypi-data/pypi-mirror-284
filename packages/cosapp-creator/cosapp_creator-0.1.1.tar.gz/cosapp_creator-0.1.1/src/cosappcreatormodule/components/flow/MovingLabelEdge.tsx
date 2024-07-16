import React, { useEffect, useState } from 'react';
import {
  BaseEdge,
  EdgeLabelRenderer,
  EdgeProps,
  getBezierPath
} from 'reactflow';

import { connectionType, FromTo, pullingType } from '../../tools/customTypes';

const arrow = '→';
const hasMapping = (name: string, mapping?: string) =>
  mapping !== undefined && name !== mapping;

const getConnMap = ({ from, to }: FromTo) =>
  hasMapping(from, to) ? from + arrow + to : from;

const getData = (props: EdgeProps) => {
  const { data } = props;
  if (!data) throw new Error(`Missing data in ${props.id}`);
  return data;
};

const getPullMap = (source: string, name: string, mapping?: string) =>
  source === 'pullingsIn'
    ? `${hasMapping(name, mapping) ? mapping + arrow : ''}${name}`
    : `${name}${hasMapping(name, mapping) ? arrow + mapping : ''}`;

type EdgeData = {
  showLabel?: boolean;
  labelPosition?: { left: number; top: number };
};

export type ConnEdgeData = { connection: connectionType } & EdgeData;
export type PullEdgeData = { pulling: pullingType } & EdgeData;
type labelData = { customLabel: string } & EdgeData;

/** Custom edge with moving label */
function MovingLabelEdge(props: EdgeProps<labelData>) {
  const [edgePath] = getBezierPath(props);
  const data: labelData = getData(props);
  const { customLabel, showLabel, labelPosition } = data;
  const { left, top } = labelPosition || { left: 0, top: 0 };

  return (
    <>
      <BaseEdge {...props} path={edgePath} />
      {showLabel ? (
        <>
          <EdgeLabelRenderer>
            <div
              className="connectionEdgeLabel"
              style={{ position: 'absolute', left, top }}
            >
              {customLabel}
            </div>
          </EdgeLabelRenderer>
        </>
      ) : (
        ''
      )}
    </>
  );
}

/** Connection edge with moving label */
export function ConnectionEdge(props: EdgeProps<ConnEdgeData>) {
  const [label, setLabel] = useState('');
  const data: ConnEdgeData = getData(props);
  const { connection, showLabel, labelPosition } = data;

  useEffect(() => {
    const { ports, variables } = connection;
    const initLabel = variables
      ? `[${variables.map(variable => getConnMap(variable)).join(', ')}]`
      : getConnMap(ports);
    setLabel(initLabel);
  }, [connection]);

  return (
    <MovingLabelEdge
      {...props}
      data={{ showLabel, labelPosition, customLabel: label }}
    />
  );
}

/** Pulling edge with moving label */
export function PullingEdge(props: EdgeProps<PullEdgeData>) {
  const [label, setLabel] = useState('');
  const { source } = props;
  const data: PullEdgeData = getData(props);
  const { pulling, showLabel, labelPosition } = data;

  useEffect(() => {
    const { port, portMapping, variables } = pulling;
    if (variables) {
      const varsLabel = variables.map(({ name, mapping }) =>
        getPullMap(source, name, mapping)
      );
      setLabel(`[${varsLabel.join(', ')}]`);
    } else {
      setLabel(getPullMap(source, port, portMapping));
    }
  }, [pulling]);

  return (
    <MovingLabelEdge
      {...props}
      data={{ showLabel, labelPosition, customLabel: label }}
    />
  );
}
