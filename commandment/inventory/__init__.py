
# These applications should not be reported on because they are part of the operating system.
DEFAULT_BUNDLE_ID_BLACKLIST = [
    'com.apple.PubSubAgent',
    'com.apple.IMServicePlugInAgent',
    'com.apple.print.PrinterProxy',
    'com.apple.speech.synthesis.SpeechSynthesisServer',
    'com.apple.FontRegistryUIAgent',
    'com.apple.AddressBook.sync',
    'com.apple.AddressBookSourceSync',
    'com.apple.AddressBook.abd',
    'com.apple.ABAssistantService',
    'com.apple.check_afp',
    'com.apple.screencapturetb',
    'com.apple.rcd',
    'com.apple.loginwindow',
    'com.apple.CloudKit.ShareBear',
    'com.apple.cloudphotosd',
    'com.apple.ZoomWindow.app',
    'com.apple.wifi.WiFiAgent',
    'com.apple.weather',
    'com.apple.UserNotificationCenter',
    'com.apple.VoiceOver',
    'com.apple.UnmountAssistantAgent',
    'com.apple.UniversalAccessControl',
    'com.apple.Ticket-Viewer',
    'com.apple.ThermalTrap',
    'com.apple.systemuiserver',
    'com.apple.systemevents',
    'com.apple.stocks',
    'com.apple.SoftwareUpdate',
    'com.apple.SocialPushAgent',
    'com.apple.SecurityFixer',
    'com.apple.ScriptMonitor',
    'com.apple.ReportPanic',
    'com.apple.RemoteDesktopAgent',
    'com.apple.pluginIM.pluginIMRegistrator',
    'com.apple.RapportUIAgent',
    'com.apple.ProblemReporter',
    'com.apple.PowerChime',
    'com.apple.Pass-Viewer',
    'com.apple.PIPAgent',
    'com.apple.OSDUIHelper',
    'com.apple.ODSAgent',
    'com.apple.OBEXAgent',
    'com.apple.notificationcenterui',
    'com.apple.NowPlayingTouchUI',
    'com.apple.NetworkDiagnostics',
    'com.apple.NetAuthAgent',
    'com.apple.MemorySlotUtility',
    'com.apple.MRT',
    'com.apple.locationmenu',
    'com.apple.Language-Chooser',
    'com.apple.security.Keychain-Circle-Notification',
    'com.apple.KeyboardSetupAssistant',
    'com.apple.JavaWebStart',
    'com.apple.JarLauncher',
    'com.apple.installer',
    'com.apple.Installer-Progress',
    'com.apple.PackageKit.Install-in-Progress',
    'com.apple.dt.CommandLineTools.installondemand',
    'com.apple.imageevents',
    'com.apple.helpviewer',
    'com.apple.gamecenter',
    'com.apple.FolderActionsDispatcher',
    'com.apple.FirmwareUpdateHelper',
    'com.apple.finder.Open-iCloudDrive',
    'com.apple.finder.Open-Network',
    'com.apple.finder.Open-Computer',
    'com.apple.finder.Open-AllMyFiles',
    'com.apple.finder.Open-AirDrop',
    'com.apple.ExpansionSlotUtility',
    'com.apple.EscrowSecurityAlert',
    'com.apple.DwellControl',
    'com.apple.dock',
    'com.apple.DiskImageMounter',
    'com.apple.DiscHelper',
    'com.apple.databaseevents',
    'com.apple.coreservices.uiagent',
    'com.apple.CoreLocationAgent',
    'com.apple.controlstrip',
    'com.apple.CaptiveNetworkAssistant',
    'com.apple.CalendarFileHandler',
    'com.apple.BluetoothUIServer',
    'com.apple.BluetoothSetupAssistant',
    'com.apple.AutomatorRunner',
    'com.apple.wifi.diagnostics',
    'com.apple.SystemImageUtility',
    'com.apple.StorageManagementLauncher',
    'com.apple.ScreenSharing',
    'com.apple.RAIDUtility',
    'com.apple.NetworkUtility',
    'com.apple.FolderActionsSetup',
    'com.apple.appleseed.FeedbackAssistant',
    'com.apple.archiveutility',
    'com.apple.AboutThisMacLauncher',
    'com.apple.AppleScriptUtility',
    'com.apple.AppleGraphicsWarning',
    'com.apple.AppleFileServer',
    'com.apple.appstore.AppDownloadLauncher',
    'com.apple.AirPortBaseStationAgent',
    'com.apple.AirPlayUIAgent',
    'com.apple.AddressBook.UrlForwarder',
    'com.apple.AVB-Audio-Configuration',
    'com.apple.ColorSyncCalibrator',
    'com.apple.SyncServices.AppleMobileSync',
    'com.apple.SyncServices.AppleMobileDeviceHelper',
    'com.apple.WebKit.PluginHost',
    'com.apple.WebProcess',
    'com.apple.WebKit.PluginProcess',
    'com.apple.WebKit.NetworkProcess',
    'com.apple.WebKit.DatabaseProcess',
    'com.apple.mrt.uiagent',
    'com.apple.WebKit.PluginHost',
    'com.apple.syncserver',
    'com.apple.ScreenSaver.Engine',
    'com.apple.QuickLookDaemon32',
    'com.apple.VoiceOverQuickstart',
    'com.apple.CharacterPaletteIM',
    'com.apple.DirectoryUtility',
    'com.apple.SetupAssistant',
    'com.apple.PhotoLibraryMigrationUtility',
    'com.apple.NetworkSetupAssistant',
    'com.apple.ManagedClient',
    'com.apple.finder',
    'com.apple.CertificateAssistant',
    'com.apple.print.add',
    'com.adobe.dynamiclinkmediaserver',
    'com.apple.Family',
    'com.apple.familycontrols.useragent',
    'com.apple.frameworks.diskimages.diuiagent',
    'com.apple.FollowUpUI',
    'com.apple.CCE.CIMFindInputCode',
    'com.apple.cmfsyncagent',
    'com.apple.storeuid',
    'com.apple.lateragent',
    'com.apple.bird',
    'com.apple.Calibration-Assistant',
    'com.apple.AOSPushRelay',
    'com.apple.AOSHeartbeat',
    'com.apple.AOSAlertManager',
    'com.apple.iCloudUserNotificationsd',
    'com.apple.TrackpadIM-Container',
    'com.apple.VIM-Container',
    'com.apple.inputmethod.Tamil',
    'com.apple.TCIM-Container',
    'com.apple.inputmethod.AssistiveControl',
    'com.apple.SCIM-Container',
    'com.apple.PAH-Container',
    'com.apple.inputmethod.PluginIM',
    'com.apple.KIM-Container',
    'com.apple.KeyboardViewer',
    'com.apple.JapaneseIM-Container',
    'com.apple.ink.inkserver',
    'com.apple.HIM-Container',
    'com.apple.inputmethod.EmojiFunctionRowItem-Container',
    'com.apple.inputmethod.ironwood',
    'com.apple.inputmethod.Ainu',
    'com.apple.50onPaletteIM',
    'com.apple.AutoImporter',
    'com.apple.VirtualScanner',
    'com.apple.Type8Camera',
    'com.apple.Type5Camera',
    'com.apple.Type4Camera',
    'com.apple.PTPCamera',
    'com.apple.MassStorageCamera',
    'com.apple.AirScanScanner',
    'com.apple.BuildWebPage',
    'com.apple.WebKit.PluginHost',
    'com.apple.cmfsyncagent',
    'com.apple.imavagent',
    'com.apple.idsfoundation.IDSRemoteURLConnectionAgent',
    'com.apple.ids.IDSCredentialsAgent',
    'com.apple.identityservicesd',
    'com.apple.imautomatichistorydeletionagent',
    'com.apple.imagent',
    'com.apple.imtransferservices.IMTransferAgent',
    'com.apple.ImageCaptureService',
    'com.apple.syncservices.syncuid',
    'com.apple.speech.SpeechDataInstallerd',
    'com.apple.eap8021x.eaptlstrust',
    'com.apple.AskPermissionUI',
    'com.apple.MakePDF',
    'com.apple.QuickLookDaemon',
    'com.apple.quicklook.ui.helper',
    'com.apple.notificationcenter.widgetsimulator',
    'com.apple.Spotlight',
    'com.apple.Siri',
    'com.apple.InstallAssistant.HighSierra',
    'com.apple.ManagedClient',
    'com.apple.InstallAssistant.HighSierra',
    'com.apple.FindMyMacMessenger',
    'com.apple.idsfoundation.IDSRemoteURLConnectionAgent',
    'com.apple.identityservicesd',
    'com.apple.imavagent',
    'com.apple.imagent',
    'com.apple.imautomatichistorydeletionagent',
    'com.apple.imtransferservices.IMTransferAgent',
    'com.apple.soagent',
    'com.apple.SyncServices.AppleMobileSync',
    'com.apple.SyncServices.AppleMobileDeviceHelper',
    'com.apple.nbagent',
    'com.apple.ScreenReaderUIServer',
    'com.apple.speech.SpeechRecognitionServer',
    'com.apple.STMFramework.UIHelper',
    'com.apple.syncservices.ConflictResolver',
    'com.apple.accessibility.universalAccessAuthWarn',
    'com.apple.accessibility.universalAccessHUD',
    'com.apple.accessibility.DFRHUD',
    'com.apple.coreservices.UASharedPasteboardProgressUI',
    'com.apple.ChineseTextConverterService',
    'com.apple.SummaryService',
]