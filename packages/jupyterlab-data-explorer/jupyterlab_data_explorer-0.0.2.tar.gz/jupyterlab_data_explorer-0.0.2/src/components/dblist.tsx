import * as React from 'react';
import { Menu, ContextMenu } from '@lumino/widgets';
import { Clipboard, InputDialog } from '@jupyterlab/apputils';
import { showDialog, Dialog } from '@jupyterlab/apputils';
import { CommandRegistry } from '@lumino/commands';
import { TranslationBundle } from '@jupyterlab/translation';
import {
  refreshIcon,
  clearIcon,
  copyIcon,
  editIcon
} from '@jupyterlab/ui-components';
import { FixedSizeList as List } from 'react-window';
import AutoSizer from 'react-virtualized-auto-sizer';

import { Loading } from './loading';
import { IDbItem, ConnType, CommentType, IComment } from '../interfaces';
import { IJpServices } from '../JpServices';
import {
  queryIcon,
  oracleIcon,
  sqlIcon,
  tabIcon,
  viewIcon,
  connAddIcon,
  hiveIcon,
  pgsqlIcon,
  mysqlIcon,
  sqliteIcon,
  deleteIcon
} from '../icons';
import {
  tbStyle,
  listStyle,
  hrStyle,
  divListStyle,
  activeStyle
} from './styles';
import { ActionBtn } from './ActionBtn';
import { getSqlModel, QueryModel } from '../model';
import { newSqlConsole } from '../sqlConsole';

type SelectFunc = (
  item: IDbItem
) => (
  ev: React.MouseEvent<HTMLLIElement | HTMLDivElement, MouseEvent>
) => Promise<void>;

type ListProps = {
  onSelect: SelectFunc;
  list: Array<IDbItem>;
  onRefresh: () => any;
  filter: string;
  wait?: boolean;
  dbid?: string;
  schema?: string;
  jp_services?: IJpServices;
  trans: TranslationBundle;
};

type ConnListProps = ListProps & { onAddConn: () => any };

/**
 * React component for rendering a panel for performing Table operations.
 */
export class ConnList extends React.Component<
  ConnListProps,
  { sel_name?: string }
> {
  constructor(props: ConnListProps) {
    super(props);
    this._contextMenu = this._createContextMenu();
    this.state = {};
  }

  private _createContextMenu(): Menu {
    const { trans } = this.props.jp_services as IJpServices;
    const commands = new CommandRegistry();
    const del = 'del';
    const clear_pass = 'clean-pass';
    const open_console = 'open-console';
    const edit = 'edit';

    commands.addCommand(open_console, {
      label: trans.__('打开数据库控制台'),
      icon: queryIcon.bindprops({ stylesheet: 'menuItem' }),
      execute: this._open_console
    });

    commands.addCommand(del, {
      label: trans.__('删除数据库连接'),
      icon: deleteIcon.bindprops({ stylesheet: 'menuItem' }),
      execute: this._del_conn
    });

    commands.addCommand(clear_pass, {
      label: trans.__('清除密码'),
      icon: clearIcon.bindprops({ stylesheet: 'menuItem' }),
      execute: this._clear_pass
    });

    commands.addCommand(edit, {
      label: trans.__('编辑注释'),
      icon: editIcon.bindprops({ stylesheet: 'menuItem' }),
      execute: this._editComment
    });

    const menu = new Menu({ commands });
    menu.addItem({ command: open_console });
    menu.addItem({ command: del });
    menu.addItem({ command: clear_pass });
    menu.addItem({ command: edit });
    return menu;
  }

  render(): React.ReactElement {
    const { onSelect, list, onAddConn, onRefresh, filter, jp_services } =
      this.props;
    const { trans } = jp_services as IJpServices;
    const { sel_name } = this.state;
    return (
      <>
        <div className={tbStyle}>
          <div style={{ textAlign: 'right' }}>
            <ActionBtn
              msg={trans.__('添加新的数据库连接')}
              icon={connAddIcon}
              onClick={onAddConn}
            />
            <ActionBtn
              msg={trans.__('刷新')}
              icon={refreshIcon}
              onClick={onRefresh}
            />
          </div>
          <hr className={hrStyle} />
        </div>
        <ul className={listStyle}>
          {list
            .filter(
              p =>
                p.name.toLowerCase().includes(filter) ||
                (p.desc && p.desc.toLowerCase().includes(filter))
            )
            .map((p, idx) => (
              <li
                key={idx}
                className={sel_name === p.name ? activeStyle : ''}
                onClick={onSelect(p)}
                title={p.name + '\n' + p.desc}
                onContextMenu={event => this._handleContextMenu(event, p)}
              >
                {(p.subtype as ConnType) === ConnType.DB_MYSQL && (
                  <mysqlIcon.react tag="span" width="16px" height="16px" />
                )}
                {(p.subtype as ConnType) === ConnType.DB_PGSQL && (
                  <pgsqlIcon.react tag="span" width="16px" height="16px" />
                )}
                {((p.subtype as ConnType) === ConnType.DB_HIVE_LDAP ||
                  (p.subtype as ConnType) === ConnType.DB_HIVE_KERBEROS) && (
                  <hiveIcon.react tag="span" width="16px" height="16px" />
                )}
                {(p.subtype as ConnType) === ConnType.DB_SQLITE && (
                  <sqliteIcon.react tag="span" width="16px" height="16px" />
                )}
                {(p.subtype as ConnType) === ConnType.DB_ORACLE && (
                  <oracleIcon.react tag="span" width="16px" height="16px" />
                )}
                <span className="name">{p.name}</span>
                <span className="memo">{p.desc}</span>
              </li>
            ))}
        </ul>
      </>
    );
  }

  private _handleContextMenu = (
    event: React.MouseEvent<any>,
    item: IDbItem
  ) => {
    this._sel_item = item;
    this._contextMenu.open(event.clientX, event.clientY);
    event.preventDefault();
    this.setState({ sel_name: item.name });
  };

  private _del_conn = async () => {
    const { trans } = this.props.jp_services as IJpServices;
    const { name } = this._sel_item;
    showDialog({
      title: trans.__('您确定?'),
      body: trans.__('删除数据库连接：') + name,
      buttons: [Dialog.cancelButton(), Dialog.okButton()]
    }).then(result => {
      if (result.button.accept) {
        getSqlModel().del_conn(name);
      }
    });
  };

  private _clear_pass = () => {
    getSqlModel().clear_pass(this._sel_item.name);
  };

  private _editComment = async () => {
    const { name, desc } = this._sel_item;
    const { trans } = this.props;
    const result = await InputDialog.getText({
      title: trans.__('输入注释: ' + name),
      text: desc
    });
    if (result.value === null || result.value === desc) {
      return;
    }
    const comment: IComment = {
      type: CommentType.C_CONN,
      dbid: name,
      comment: result.value || ''
    };
    getSqlModel().add_comment(comment);
  };

  private _open_console = () => {
    const qmodel = new QueryModel({
      dbid: this._sel_item.name,
      conn_readonly: true
    });
    newSqlConsole(qmodel, '', this.props.jp_services as IJpServices);
  };

  private readonly _contextMenu: Menu;
  private _sel_item!: IDbItem;
}

export class SchemaList extends React.Component<
  ListProps,
  { sel_name?: string }
> {
  constructor(props: ListProps) {
    super(props);
    this._contextMenu = this._createContextMenu();
    this.state = {
      sel_name: ''
    };
  }

  private _createContextMenu(): ContextMenu {
    const { trans } = this.props;
    const commands = new CommandRegistry();
    const copy = 'copyName';
    const copy_all = 'copyAll';
    const open_console = 'open-console';
    const edit = 'edit';
    commands.addCommand(open_console, {
      label: trans.__('打开数据库控制台'),
      icon: queryIcon.bindprops({ stylesheet: 'menuItem' }),
      execute: this._open_console
    });
    commands.addCommand(copy, {
      label: trans.__('复制表名称'),
      icon: copyIcon.bindprops({ stylesheet: 'menuItem' }),
      execute: this._copyToClipboard('n')
    });
    commands.addCommand(copy_all, {
      label: trans.__('复制表名称 & Comment'),
      icon: copyIcon.bindprops({ stylesheet: 'menuItem' }),
      execute: this._copyToClipboard('all')
    });
    commands.addCommand(edit, {
      label: trans.__('编辑注释'),
      icon: editIcon.bindprops({ stylesheet: 'menuItem' }),
      execute: this._editComment
    });
    const menu = new ContextMenu({ commands });
    menu.addItem({ command: copy, selector: '[data-ptype="table"]', rank: 50 });
    menu.addItem({
      command: copy_all,
      selector: '[data-ptype="table"]',
      rank: 50
    });
    menu.addItem({
      command: open_console,
      selector: '*[data-ptype]',
      rank: 100
    });
    menu.addItem({ command: edit, selector: '*[data-ptype]', rank: 100 });
    return menu;
  }

  render(): React.ReactElement {
    const { trans, onSelect, list, onRefresh, filter, wait } = this.props;
    const { sel_name } = this.state;

    const l = list.filter(
      p =>
        p.name.toLowerCase().includes(filter) ||
        (p.desc && p.desc.toLowerCase().includes(filter))
    );

    const Row = ({
      index,
      style,
      data
    }: {
      index: number;
      style: React.CSSProperties;
      data: any;
    }) => {
      const p = data[index];
      return (
        <div
          key={index}
          style={style}
          onClick={onSelect(p)}
          title={p.name + '\n' + p.desc}
          className={
            divListStyle + (sel_name === p.name ? ' ' + activeStyle : '')
          }
          data-ptype={p.type}
          onContextMenu={event => this._handleContextMenu(event, p)}
        >
          {p.type === 'db' && (
            <sqlIcon.react
              tag="span"
              width="16px"
              height="16px"
              verticalAlign="text-top"
            />
          )}
          {p.type === 'table' && p.subtype !== 'V' && (
            <tabIcon.react
              tag="span"
              width="16px"
              height="16px"
              verticalAlign="text-top"
            />
          )}
          {p.type === 'table' && p.subtype === 'V' && (
            <viewIcon.react
              tag="span"
              width="16px"
              height="16px"
              verticalAlign="text-top"
            />
          )}
          <span className="name">{p.name}</span>
          <span className="memo">{p.desc}</span>
        </div>
      );
    };
    return (
      <>
        <div className={tbStyle}>
          <div style={{ textAlign: 'right' }}>
            <ActionBtn
              msg={trans.__('refresh')}
              icon={refreshIcon}
              onClick={onRefresh}
            />
          </div>
          <hr className={hrStyle} />
        </div>
        {wait ? (
          <Loading />
        ) : (
          <AutoSizer>
            {({ height, width }: { height: any; width: any }) => (
              <List
                itemCount={l.length}
                itemData={l}
                itemSize={25}
                height={height - 120}
                width={width}
              >
                {Row}
              </List>
            )}
          </AutoSizer>
        )}
      </>
    );
  }

  private _handleContextMenu = (
    event: React.MouseEvent<any>,
    item: IDbItem
  ) => {
    event.preventDefault();
    this._sel_item = item;
    this.setState({ sel_name: item.name });
    this._contextMenu.open(event.nativeEvent); //event.clientX, event.clientY);
  };

  private _copyToClipboard = (t: string) => () => {
    const { name, desc } = this._sel_item;
    const comment = desc?.trim();
    if (t === 'all' && comment !== '') {
      Clipboard.copyToSystem(`${name} /* ${comment} */`);
    } else {
      Clipboard.copyToSystem(`${name}`);
    }
  };

  private _open_console = () => {
    const qmodel = new QueryModel({
      dbid: this.props.dbid as string,
      conn_readonly: true
    });
    newSqlConsole(qmodel, '', this.props.jp_services as IJpServices);
  };

  private _editComment = async () => {
    const { dbid } = this.props;
    const { name, desc } = this._sel_item;
    const { trans } = this.props;
    const result = await InputDialog.getText({
      title: trans.__('输入注释: ' + name),
      text: desc
    });
    if (result.value === null || result.value === desc) {
      return;
    }
    const comment: IComment = {
      type: CommentType.C_SCHEMA,
      dbid: dbid as string,
      schema: name,
      comment: result.value || ''
    };
    if (this._sel_item.type === 'table') {
      (comment.type = CommentType.C_TABLE), (comment.schema = '');
      comment.table = name;
    }
    getSqlModel().add_comment(comment);
  };

  private readonly _contextMenu: ContextMenu;
  private _sel_item!: IDbItem;
}

export class TbList extends React.Component<ListProps, { sel_name?: string }> {
  constructor(props: ListProps) {
    super(props);
    this._contextMenu = this._createContextMenu();
    this.state = {
      sel_name: ''
    };
  }

  private _createContextMenu(): Menu {
    const { trans } = this.props;
    const commands = new CommandRegistry();
    const copy = 'copyName';
    const copy_all = 'copyAll';
    const open_console = 'open-console';
    const edit = 'edit';
    commands.addCommand(open_console, {
      label: trans.__('打开数据库控制台'),
      icon: queryIcon.bindprops({ stylesheet: 'menuItem' }),
      execute: this._open_console
    });
    commands.addCommand(copy, {
      label: trans.__('复制表名称'),
      icon: copyIcon.bindprops({ stylesheet: 'menuItem' }),
      execute: this._copyToClipboard('n')
    });
    commands.addCommand(copy_all, {
      label: trans.__('复制表名称和注释'),
      icon: copyIcon.bindprops({ stylesheet: 'menuItem' }),
      execute: this._copyToClipboard('all')
    });
    commands.addCommand(edit, {
      label: trans.__('编辑注释'),
      icon: editIcon.bindprops({ stylesheet: 'menuItem' }),
      execute: this._editComment
    });
    const menu = new Menu({ commands });
    menu.addItem({ command: open_console });
    menu.addItem({ command: edit });
    menu.addItem({ command: copy });
    menu.addItem({ command: copy_all });
    return menu;
  }

  render(): React.ReactElement {
    const { trans, onSelect, list, onRefresh, filter, wait } = this.props;

    const { sel_name } = this.state;

    const l = list.filter(
      p =>
        p.name.toLowerCase().includes(filter) ||
        (p.desc && p.desc.toLowerCase().includes(filter))
    );

    const Row = ({
      index,
      style,
      data
    }: {
      index: number;
      style: React.CSSProperties;
      data: any;
    }) => {
      const p = data[index];
      return (
        <div
          key={index}
          style={style}
          onClick={onSelect(p)}
          title={p.name + '\n' + p.desc}
          className={
            divListStyle + ' ' + (sel_name === p.name ? activeStyle : '')
          }
          onContextMenu={event => this._handleContextMenu(event, p)}
        >
          {p.type === 'table' && p.subtype !== 'V' && (
            <tabIcon.react
              tag="span"
              width="14px"
              height="14px"
              right="5px"
              verticalAlign="text-top"
            />
          )}
          {p.type === 'table' && p.subtype === 'V' && (
            <viewIcon.react
              tag="span"
              width="16px"
              height="16px"
              verticalAlign="text-top"
            />
          )}
          <span className="name">{p.name}</span>
          <span className="memo">{p.desc}</span>
        </div>
      );
    };

    return (
      <>
        <div className={tbStyle}>
          <div style={{ textAlign: 'right' }}>
            <ActionBtn
              msg={trans.__('refresh')}
              icon={refreshIcon}
              onClick={onRefresh}
            />
          </div>
          <hr className={hrStyle} />
        </div>
        {wait ? (
          <Loading />
        ) : (
          <AutoSizer>
            {({ height, width }: { height: any; width: any }) => (
              <List
                itemCount={l.length}
                itemData={l}
                itemSize={25}
                height={height - 120}
                width={width}
              >
                {Row}
              </List>
            )}
          </AutoSizer>
        )}
      </>
    );
  }

  private _handleContextMenu = (
    event: React.MouseEvent<any>,
    item: IDbItem
  ) => {
    event.preventDefault();
    this._sel_item = item;
    this.setState({ sel_name: item.name });
    this._contextMenu.open(event.clientX, event.clientY);
  };

  private _copyToClipboard = (t: string) => () => {
    const { name, desc } = this._sel_item;
    const { schema } = this.props;
    const comment = desc?.trim();
    if (t === 'all' && comment !== '') {
      Clipboard.copyToSystem(`${schema}.${name} /* ${comment} */`);
    } else {
      Clipboard.copyToSystem(`${schema}.${name}`);
    }
  };

  private _open_console = () => {
    const qmodel = new QueryModel({
      dbid: this.props.dbid as string,
      conn_readonly: true
    });
    newSqlConsole(qmodel, '', this.props.jp_services as IJpServices);
  };

  private _editComment = async () => {
    const { dbid, schema } = this.props;
    const { name, desc } = this._sel_item;
    const { trans } = this.props;
    const result = await InputDialog.getText({
      title: trans.__('输入注释: ' + name),
      text: desc
    });
    if (result.value === null || result.value === desc) {
      return;
    }
    const comment: IComment = {
      type: CommentType.C_TABLE,
      dbid: dbid as string,
      schema,
      table: name,
      comment: result.value || ''
    };
    getSqlModel().add_comment(comment);
  };

  private readonly _contextMenu: Menu;
  private _sel_item!: IDbItem;
}
