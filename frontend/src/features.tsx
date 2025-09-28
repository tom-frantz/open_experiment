import type {ReactNode} from "react";
import {OpenFeature, OpenFeatureProvider} from '@openfeature/react-sdk';
import { FlagsmithClientProvider } from '@openfeature/flagsmith-client-provider';

const flagsmithClientProvider = new FlagsmithClientProvider({
    environmentID: 'your_client_side_environment_key',
    api: "localhost:8800/api/v1/",
    cacheFlags: true,
    cacheOptions: {
        skipAPI: true,
    },
});
OpenFeature.setProvider(flagsmithClientProvider);

export interface FeatureFlagProviderProps {
    children: ReactNode;
}

export const FeatureFlagProvider = ({children}: FeatureFlagProviderProps) => {
    return <OpenFeatureProvider>
        {children}
    </OpenFeatureProvider>
}