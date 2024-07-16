import { useMemo } from 'react';
import { CoSAppCreatorProps } from './CoSAppCreator.types';
import { CoSAppCreatorWidget } from './components/CoSAppCreatorWidget';
import { ApiClient } from './tools/apiTool';

export function CoSAppCreator(props: CoSAppCreatorProps): JSX.Element {
  const apiClient = useMemo(() => {
    const baseURL = props.baseUrl ?? 'http://127.0.0.1:8000';
    const client = new ApiClient({ baseURL });
    client;
    console.log(`Using cosapp_creator_api at ${baseURL}`);

    return client;
  }, [props.baseUrl]);

  return <CoSAppCreatorWidget apiClient={apiClient} />;
}
